
from app.type.Video import Video,thumbnail,keywordList
from app.type.Interactions import Interactions


class Deserialise:
    @staticmethod
    def videoData(raw:dict) -> dict:
        # videoData=Video()
        videoData=Video()
            
        videoData['videoId']=raw['videoDetails']['videoId']
        videoData['title']=raw['videoDetails']['title']
        videoData['author']=raw['videoDetails']['author']
        videoData['lengthSeconds']=raw['videoDetails']['lengthSeconds']
        videoData['keywords']=keywordList(iterable)(raw['videoDetails']['keywords'])
        videoData['channelId']=raw['videoDetails']['channelId']
        videoData['shortDescription']=raw['videoDetails']['shortDescription']
        videoData['viewCount']=int(raw['videoDetails']['viewCount'])
        videoData['thumbnail']=thumbnail(raw['videoDetails']['thumbnail']['thumbnails'][-1])
        
        videoData['isOwnerViewing']=True if raw['videoDetails']['isOwnerViewing']=='true' else False
        videoData['isCrawlable']=True if raw['videoDetails']['isCrawlable'] else False
        videoData['allowRatings']=True if raw['videoDetails']['allowRatings'] else False
        videoData['isPrivate']=True if raw['videoDetails']['isPrivate'] else False
        videoData['isLiveContent']=True if raw['videoDetails']['isLiveContent'] else False
        if 'microformat' in raw.keys():
            videoData['country']=raw['microformat']['playerMicroformatRenderer']['availableCountries']
        return videoData

    @staticmethod
    def interactionData(raw:dict):
        interactions=Interactions()
        content=raw['contents']['twoColumnWatchNextResults']['results']['results']['contents']
        # getting likes
        filteredLikeSection=content[0]['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']
        # filtering like subtext
        likeText=filteredLikeSection['defaultText']['accessibility']['accessibilityData']['label']
        
        interactions['likes']=int(''.join([i for i in likeText if str.isdigit(i)]))    #Coz f* regex
        interactions['comments_continuation']=content[3]['itemSectionRenderer']['contents'][0]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
        
        return interactions
    
        
    
