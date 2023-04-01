from app.type.common import img,strList,strbool,dateInt
from app.dataHandler.helper import convert_to_number,filterInt
from app.type.channel.Channel import tabEndpoints,Channel
from app.type.channel.about import aboutChannel
def deserialise_channelDetails(raw:dict)->Channel:
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

def deserialise_channelHome(raw:dict):
    
    raw['continuationContents']['sectionListContinuation']
def deserialise_channelAbout(raw:dict):
    content=raw['continuationContents']['sectionListContinuation']['contents'][0]['itemSectionRenderer']['contents'][0]
    
    aboutChannel=aboutChannel()
    if 'description' in content.keys():
        aboutChannel['description']=str(content['description']['simpleText'])
    if 'viewCountText' in content.keys():
        aboutChannel['viewCount']=filterInt(content['viewCountText']['simpleText'])
    if 'joinedDateText' in content.keys():
        aboutChannel['joinedDate']=dateInt(content['joinedDateText']['runs'][-1]['text'])
    if 'country' in content.keys():
        aboutChannel['country']=str(content['country']['simpleText'])
    
    # TODO: To be tested
    # tabs=raw['contents']['twoColumnBrowseResultsRenderer']['tabs']
    # tab =   [i for i in tabs if 'selected' in i['tabRenderer'].keys() and i['tabRenderer']['selected']=='true']
    # content=tab[0]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['channelAboutFullMetadataRenderer']
    # aboutChannel=aboutChannel()
    return aboutChannel

def deserialise_channelVideos(raw:dict):
    tabs=   raw['contents']['twoColumnBrowseResultsRenderer']['tabs']
    tab=   [i for i in tabs if 'selected' in i['tabRenderer'].keys() and i['tabRenderer']['selected']=='true']
    
    contents=tab[0]['content']['richGridRenderer']['contents']
    for video in contents:
        video=video['richItemRenderer']['content']['videoRenderer']
        # ['videoId']['thumbnail']['thumbnails'][-1]
        









