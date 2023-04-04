from app.dataclass.ChannelDataClasses.ChannelMeta import Channel, ChannelTiny, tabEndpoints
from app.dataclass.common import dateInt, img, publishTime, strbool, strList, url
from app.DataEngine.helper import convert_to_number, filterInt
from app.dataclass.VideoDataClasses.videoMini import channelVideos, sort, videoMini
from app.helperLib.time_to_seconds import t2sec
import time




def deserialise_channelDetails(raw:dict)->Channel:
    channelData=Channel()
    channelData['channelId']                        =   str(raw['header']['c4TabbedHeaderRenderer']['channelId'])
    channelData['title']                            =   str(raw['header']['c4TabbedHeaderRenderer']['title'])
    channelData['banner']                           =   img(**raw['header']['c4TabbedHeaderRenderer']['banner']['thumbnails'][-1])
    channelData['tvBanner']                         =   img(**raw['header']['c4TabbedHeaderRenderer']['tvBanner']['thumbnails'][-1])
    channelData['channelHandle']                    =   str(raw['header']['c4TabbedHeaderRenderer']['channelHandleText']['runs'][0]['text'])
    channelData['tagline']                          =   str(raw['header']['c4TabbedHeaderRenderer']['tagline']['channelTaglineRenderer']['content'])
    channelData['subscriberCountApprox']            =   convert_to_number(raw['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText'])
    channelData['videosCount']                      =   int(raw['header']['c4TabbedHeaderRenderer']['videosCountText']['runs'][0]['text'])

    channelData['description']                      =   str(raw['metadata']['channelMetadataRenderer']['description'])
    channelData['avatar']                           =   img(**raw['metadata']['channelMetadataRenderer']['avatar']['thumbnails'][-1])

    if 'availableCountryCodes' in raw['metadata']['channelMetadataRenderer'].keys():
        channelData['availableCountry']             =   strList(raw['metadata']['channelMetadataRenderer']['availableCountryCodes'])
    channelData['isFamilySafe']                     =   strbool(raw['metadata']['channelMetadataRenderer']['isFamilySafe'])
    
    channelData['isnoindex']                        =   strbool(raw['microformat']['microformatDataRenderer']['noindex'])
    channelData['isunlisted']                       =   strbool(raw['microformat']['microformatDataRenderer']['unlisted'])
    if 'tags' in raw['microformat']['microformatDataRenderer'].keys():
        channelData['tags']                         =   strList(raw['microformat']['microformatDataRenderer']['tags'])
        
    for endpoints in raw['contents']['twoColumnBrowseResultsRenderer']['tabs'][:-1:]:
            tab= tabEndpoints()
            tab['title']                            =   str(endpoints['tabRenderer']['title'])
            tab['selected']                         =   strbool(endpoints['tabRenderer']['selected']) if 'selected' in endpoints['tabRenderer'] else strbool()
            tab['params']                           =   str(endpoints['tabRenderer']['endpoint']['browseEndpoint']['params'])
            
            channelData['tabs'].append(tab)
            
    endpoints=raw['contents']['twoColumnBrowseResultsRenderer']['tabs'][-1]['expandableTabRenderer']
    tab= tabEndpoints()
    tab['title']=str(endpoints['title'])
    tab['selected']=strbool(endpoints['selected']) if 'selected' in endpoints else strbool()
    tab['params']=str(endpoints['endpoint']['browseEndpoint']['params'])
    channelData['tabs'].append(tab)

    return channelData

def deserialise_channelTiny(raw:dict)->ChannelTiny:
    ChannelData=ChannelTiny()
    ChannelData.channelId                   =   str(raw['channelId'])
    ChannelData.channelId                   =   img(**raw['thumbnail']['thumbnails'][-1])
    ChannelData.channelId                   =   int(filterInt(raw['videoCountText']['runs'][0]['text']))
    ChannelData.channelId                   =   int(convert_to_number(raw['subscriberCountText']['simpleText']))
    ChannelData.title                       =   str(raw['title']['simpleText'])
    ChannelData.isVerified                  =   bool('ownerBadges' in raw)
    
def deserialise_channelHome(raw:dict):
    
    sectionListContinuation=raw['continuationContents']['sectionListContinuation']
    
    for Section in sectionListContinuation['contents']:
    # Getting into Item sections
        Section['itemSectionRenderer']['itemSectionRenderer']
        # channelFeaturedContentRenderer
    
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
    
    return aboutChannel


def deserialise_videoTiny(videoRender:dict):
    videoData=videoMini()
    
    videoData.videoId                           =   str(videoRender['videoId'])
    videoData.thumbnail                         =   img(**videoRender['thumbnail']['thumbnails'][-1])
    videoData.title                             =   str(videoRender['title']['runs'][0]['text'])
    videoData.length                            =   int(t2sec(videoRender['lengthText']['simpleText']))
    videoData.viewCount                         =   filterInt((videoRender['viewCountText']['simpleText']))
    
    if 'richThumbnail' in videoRender.keys():
        videoData.preview                       =   url(videoRender['richThumbnail']['movingThumbnailRenderer']['movingThumbnailDetails']['thumbnails'][-1]['url'])
    
    videoData.publishedTime.publishedTimeText   =   videoRender['publishedTimeText']['simpleText']
    videoData.publishedTime.since               =   time.time()
    
    if 'ownerBadges' in videoRender:
        videoData.ownerBadges=True
    
    return videoData


def deserialise_channelVideos(raw:dict):
    
    richGrid=raw['continuationContents']['richGridContinuation']
    chvdoData=channelVideos()
        
    # adding videos to the list
    for richItem in richGrid['contents'][:-1:]:
        videoRender=richItem['richItemRenderer']['content']['videoRenderer']
        videoData=deserialise_videoTiny(videoRender)
        chvdoData.videos.append(videoData)
        
    if 'continuationItemRenderer' in richGrid['contents'][-1]:
        chvdoData.videoContinuation=richGrid['contents'][-1]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
    else:
        videoRender=richItem['richItemRenderer']['content']['videoRenderer']
        videoData=deserialise_videoTiny(videoRender)
        chvdoData.videos.append(videoData)
    
    # Adding filteration and sort data
    for continuation in richGrid['header']['feedFilterChipBarRenderer']['contents']:
        if continuation['chipCloudChipRenderer']['text']['simpleText']=='Latest':
            chvdoData.latestContinuation=continuation['chipCloudChipRenderer']['navigationEndpoint']['continuationCommand']['token']
            if strbool(continuation['chipCloudChipRenderer']['isSelected']):
                chvdoData.sortBy=sort.latest
                
        elif continuation['chipCloudChipRenderer']['text']['simpleText']=='Popular':
            chvdoData.latestContinuation=continuation['chipCloudChipRenderer']['navigationEndpoint']['continuationCommand']['token']
            if strbool(continuation['chipCloudChipRenderer']['isSelected']):
                chvdoData.sortBy=sort.Popular
         
    return chvdoData

# def deserialise_channelShorts(raw:dict):
#     # Filtering to content level
    
#     sectionList=raw['continuationContents']['sectionListContinuation']['contents']
#     for section in sectionList[:-1:]:
#         section['channelVideoPlayerRenderer']['']
def deserialise_channelShortsTab(raw:dict):
    pass


def deserialise_channelHome(raw:dict):
        # Filtering to the contents
        homeData=dict()
        sectionList=raw['continuationContents']['sectionListContinuation']['contents']
        for section in sectionList:
            for item in section['itemSectionRenderer']['contents']:
                for key,value in item.items():
                    if key=="channelVideoPlayerRenderer":
                        shelf=dict()
                        shelf['category']="channelVideoPlayerRenderer"
                        shelf['data'].append(homeData(videoMini(value)))
                    elif key=="recognitionShelfRenderer":
                        continue
                    elif key=="shelfRenderer":
                        
                        url=value['endpoint']['commandMetadata']['webCommandMetadata']['url']
                        category=value['endpoint']['commandMetadata']['webCommandMetadata']['webPageType']
                        browseId=value['endpoint']['commandMetadata']['browseEndpoint']
                        #playlist shelf specific
                        
                        data=list()
                        for gridVideoRenderer in value['content']['horizontalListRenderer']['items']:
                            data.append(deserialise_videoTiny(gridVideoRenderer['gridVideoRenderer']))
                            
                        subtitle=value['subtitle']['simpleText']

                        



