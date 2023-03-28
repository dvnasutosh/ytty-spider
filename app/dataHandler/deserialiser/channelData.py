from app.type.common import img,strList,strbool
from app.dataHandler.helper import convert_to_number
from app.type.channel import tabEndpoints,Channel

def deserialise_channelDetails(raw:dict):
    channelData=Channel()
    channelData['channelId']=str(raw['header']['c4TabbedHeaderRenderer']['channelId'])
    channelData['title']=str(raw['header']['c4TabbedHeaderRenderer']['title'])
    channelData['banner']=img(**raw['header']['c4TabbedHeaderRenderer']['banner']['thumbnails'][-1])
    channelData['tvBanner']=img(**raw['header']['c4TabbedHeaderRenderer']['tvBanner']['thumbnails'][-1])
    channelData['channelHandle']=str(raw['header']['c4TabbedHeaderRenderer']['channelHandleText']['runs'][0]['text'])
    channelData['tagline']=str(raw['header']['c4TabbedHeaderRenderer']['tagline']['channelTaglineRenderer']['content'])
    channelData['subscriberCountApprox']=convert_to_number(raw['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText'])
    channelData['videosCount']=int(raw['header']['c4TabbedHeaderRenderer']['videosCountText']['runs'][0]['text'])
    
    channelData['description']=str(raw['metadata']['channelMetadataRenderer']['description'])
    channelData['avatar']=img(**raw['metadata']['channelMetadataRenderer']['avatar']['thumbnails'][-1])

    if 'availableCountryCodes' in raw['metadata']['channelMetadataRenderer'].keys():
        channelData['availableCountry']=strList(raw['metadata']['channelMetadataRenderer']['availableCountryCodes'])
    channelData['isFamilySafe']=strbool(raw['metadata']['channelMetadataRenderer']['isFamilySafe'])
    
    channelData['isnoindex']=strbool(raw['microformat']['microformatDataRenderer']['noindex'])
    channelData['isunlisted']=strbool(raw['microformat']['microformatDataRenderer']['unlisted'])
    if 'tags' in raw['microformat']['microformatDataRenderer'].keys():
        channelData['tags']=strList(raw['microformat']['microformatDataRenderer']['tags'])
    for endpoints in raw['contents']['twoColumnBrowseResultsRenderer']['tabs'][:-1:]:
            tab= tabEndpoints()
            tab['title']=str(endpoints['tabRenderer']['title'])
            tab['selected']=strbool(endpoints['tabRenderer']['selected']) if 'selected' in endpoints['tabRenderer'] else strbool()
            tab['params']=str(endpoints['tabRenderer']['endpoint']['browseEndpoint']['params'])
            
            channelData['tabs'].append(tab)
    endpoints=raw['contents']['twoColumnBrowseResultsRenderer']['tabs'][-1]['expandableTabRenderer']
    tab= tabEndpoints()
    tab['title']=str(endpoints['title'])
    tab['selected']=strbool(endpoints['selected']) if 'selected' in endpoints else strbool()
    tab['params']=str(endpoints['endpoint']['browseEndpoint']['params'])
    channelData['tabs'].append(tab)

    return channelData