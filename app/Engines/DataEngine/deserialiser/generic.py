
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

            #   sorting endpoints deserialisation
            
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
            shelf=ShelfDetails()
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
            data.append({'continuation':value['continuationCommand']['token']})
            
        #  deserialise smallest pieces of this youtube puzzle
        elif key in videoMiny_indicators:
            data.append(deserialise_videoMini(value))
        
        elif key in playlistMini_indicator:
            data.extend(deserialise_playlistMini(value))
        
        elif key == 'channelAboutFullMetadataRenderer':
            #  deserialise channel about
            data.append(deserialise_channelAbout(value))
        
        elif key=='verticalProductCardRenderer':
            data.append(deserialise_Product(value))
        
        elif key=='backstagePostRenderer':
            dataList.append(deserialise_backstagePostRenderer(value))
        
        elif key=='guideEntryRenderer':
            dataList.append(deserialise_guideEntryRenderer(value))
        
        else: continue
        break;
    
    return data
