import typing
from app.Engines.DataEngine.deserialiser.channelData import deserialise_Product, deserialise_backstagePostRenderer, deserialise_channelAbout, deserialise_guideEntryRenderer, deserialise_playlistMini, deserialise_videoMini
from app.dataclass.channelDC.ChannelMeta import browseEndpoint
from app.dataclass.channelDC.Content import Content, Sort, contentList
from app.dataclass.channelDC.Shelf import ShelfDetails
from app.dataclass.common import strbool
from betterdataclass import StrictDictionary


content_s_indicators=['sectionListRenderer','tabRenderer','itemSectionRenderer','richGridRenderer','richItemRenderer']
items_indicators=['gridRenderer','horizontalListRenderer','guideSectionRenderer']
videoMiny_indicators=['channelVideoPlayerRenderer','videoRenderer','gridVideoRenderer','reelItemRenderer']
playlistMini_indicator=['playlistRenderer','playlistRenderer']


def deserialise_contentGeneric(content: dict):
    dataList=contentList()
    
    # if content exists
    for key,value in content.items():
        if key in  content_s_indicators:
            data=Content()
            
            #checking if it has cont or contents
            if 'content' in value.keys():
                data['data'].extend( deserialise_contentGeneric(value))
            elif 'contents' in value.keys():
                for each in value['contents']:
                    data['data'].extend( deserialise_contentGeneric(each))

            #   sorting endpoints deserialization
            
            if 'header' in value.keys():
                for sort in value['header']['feedFilterChipBarRenderer']['contents']:
                    
                    sortBy=Sort()
                    sortBy['continuation'] = sort['chipCloudChipRenderer']['navigationEndpoint']['continuationCommand']['token']
                    sortBy['isSelected'] = strbool(sort['chipCloudChipRenderer']['isSelected'])
                    sortBy['sortType'] = sort['chipCloudChipRenderer']['text']['simpleText']
                    data['sort'] = sortBy
            
            
            dataList.append(data)
            break
        
        elif key == 'shelfRenderer':
            shelf = ShelfDetails()
            if 'title' in value.keys():
                if 'runs' in value['title']:
                    shelf.title=value['title']['runs'][0]['text']
                if 'simpleText' in value['title']:
                    shelf.title=value['simpleText']
            
            if 'endpoint' in value.keys():
                shelf.browseEndpoint=browseEndpoint(**value['endpoint']['browseEndpoint'])
            if 'subtitle' in value:
                shelf.subtitle =value['subtitle']['simpleText']
            
            if 'content' in value.keys():
                shelf.data.extend( deserialise_contentGeneric(value['content']))
            
            if 'contents' in value.keys():
                for each in value['contents']:
                    shelf.data.extend(deserialise_contentGeneric(each))
                
            dataList.append(shelf)
            break
        
        elif key == 'backstagePostThreadRenderer':
            dataList.extend(deserialise_contentGeneric(value['post']))
        
        elif key in items_indicators:
            if 'items' in value.keys():
                for each in value['items']:
                    dataList.extend( deserialise_contentGeneric(each))
        elif key=='items':
                for each in value['items']:
                    dataList.extend( deserialise_contentGeneric(each))
            
        elif key=='continuationEndpoint':
            dataList.append({'continuation':value['continuationCommand']['token']})
            
        #  deserialise smallest pieces of this youtube puzzle
        elif key in videoMiny_indicators:
            dataList.append(deserialise_videoMini(value))
        
        elif key in playlistMini_indicator:
            dataList.extend(deserialise_playlistMini(value))
        
        elif key == 'channelAboutFullMetadataRenderer':
            #  deserialise channel about
            dataList.append(deserialise_channelAbout(value))
        
        elif key=='verticalProductCardRenderer':
            dataList.append(deserialise_Product(value))
        
        elif key=='backstagePostRenderer':
            dataList.append(deserialise_backstagePostRenderer(value))
        
        elif key=='guideEntryRenderer':
            dataList.append(deserialise_guideEntryRenderer(value))
        
        else: continue
        break;
    
    return dataList





class deserializerTool(StrictDictionary):
    deserializer:typing.Callable
    keyList:typing.List[str]
    
def Udeserializer(content:dict,deserializer:typing.List[deserializerTool]):
    out={}
    def extractor_recursion(contentI:dict,deserializerI:typing.List[deserializerTool]):
        for k,v in contentI.items():
            for targets in deserializerI:
                if k in targets.keyList:
                    out[k]=targets.deserializer(v)
                    

def generic(raw,endNode):
    pass




def key_extractor(data:dict,**kv):
    
    out={}
    
    
    def extractor_recursion(data2:dict,**kv2):
        '''
        This is the recursion function.
            
        '''
        for k,v in data2.items():
            if k in kv2:
                out[k]=v
            elif isinstance(v,dict):
                return extractor_recursion(data2=data2,**kv2)
            elif isinstance(v,(list,set,tuple)):
                for item in v:
                    temp=extractor_recursion(data2=item,**kv2)
                    if temp:
                        out[k]=temp
    
    extractor_recursion(data2=data,kv2=kv)
    return out

