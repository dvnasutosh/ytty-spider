from app.Engines.DataEngine.helper import filterInt
from app.dataclass.videoDC.Video import Interactions, Video,liveBroadcast
from app.dataclass.common import img,strbool,dateInt

def deserialise_videoDetails(raw:dict) -> Video:
    """
    Deserialise Video details into a more structured format.
    """
    videoDetails=Video()

    videoDetails['videoId']                            =   raw['videoDetails']['videoId']
    videoDetails['title']                              =   raw['videoDetails']['title']
    videoDetails['author']                             =   raw['videoDetails']['author']
    videoDetails['lengthSeconds']                      =   raw['videoDetails']['lengthSeconds']
    videoDetails['keywords']                           =   list(raw['videoDetails']['keywords']) if 'keywords' in raw['videoDetails'].keys() else []
    videoDetails['channelId']                          =   raw['videoDetails']['channelId']
    videoDetails['shortDescription']                   =   raw['videoDetails']['shortDescription']
    videoDetails['viewCount']                          =   int(raw['videoDetails']['viewCount'])

    videoDetails['thumbnail']                          =   img(**raw['videoDetails']['thumbnail']['thumbnails'][-1])

    videoDetails['isOwnerViewing']                     =   strbool(raw['videoDetails']['isOwnerViewing'])
    videoDetails['isCrawlable']                        =   strbool(raw['videoDetails']['isCrawlable']) 
    videoDetails['allowRatings']                       =   strbool(raw['videoDetails']['allowRatings']) 
    videoDetails['isPrivate']                          =   strbool(raw['videoDetails']['isPrivate']) 
    videoDetails['isLiveContent']                      =   strbool(raw['videoDetails']['isLiveContent'])
    
    videoDetails['isUnlisted']                         =   strbool(raw['microformat']['playerMicroformatRenderer']['isUnlisted'])
    videoDetails['hasYpcMetadata']                     =   strbool(raw['microformat']['playerMicroformatRenderer']['hasYpcMetadata'])
    videoDetails['isFamilySafe']                       =   strbool(raw['microformat']['playerMicroformatRenderer']['isFamilySafe'])
    videoDetails['category']                           =   str(raw['microformat']['playerMicroformatRenderer']['category'])
    videoDetails['publishDate']                        =   dateInt(raw['microformat']['playerMicroformatRenderer']['publishDate'])
    videoDetails['uploadDate']                         =   dateInt(raw['microformat']['playerMicroformatRenderer']['uploadDate'])
    
    if 'availableCountries' in raw['microformat']['playerMicroformatRenderer'].keys():
        videoDetails['availableCountries']             =   list(raw['microformat']['playerMicroformatRenderer']['availableCountries'])
    
    if 'liveBroadcastDetails' in raw['microformat']['playerMicroformatRenderer'].keys():
        videoDetails['liveBroadcastDetails']           =   liveBroadcast(**raw['microformat']['playerMicroformatRenderer']['liveBroadcastDetails'])

    return videoDetails

def deserialise_interactionData(raw:dict):
    """
    Returns deserialised and Interaction data. i.e. Likes, commentsCount
    """
    interactions=Interactions()
    content=raw['contents']['twoColumnWatchNextResults']['results']['results']['contents']
    # getting likes
    filteredLikeSection=content[0]['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']
    # filtering like subtext
    likeText=filteredLikeSection['defaultText']['accessibility']['accessibilityData']['label']
    
    interactions['likes']                           =       filterInt(likeText)    #Coz f* regex
    interactions['comments_continuation']           =       content[3]['itemSectionRenderer']['contents'][0]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
    
    return interactions
    