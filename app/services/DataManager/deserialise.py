# from app.type.Video import Video

def deserialise_videoData(raw:dict) -> dict:
    # videoData=Video()
    videoData=dict()
        
    videoData['videoId']=raw['videoDetails']['videoId']
    videoData['title']=raw['videoDetails']['title']
    videoData['author']=raw['videoDetails']['author']
    videoData['lengthSeconds']=raw['videoDetails']['lengthSeconds']
    videoData['keywords']=raw['videoDetails']['keywords']
    videoData['channelId']=raw['videoDetails']['channelId']
    videoData['shortDescription']=raw['videoDetails']['shortDescription']
    videoData['viewCount']=raw['videoDetails']['viewCount']
    videoData['thumbnail']=raw['videoDetails']['thumbnail']['thumbnails'][-1]
    
    videoData['isOwnerViewing']=True if raw['videoDetails']['isOwnerViewing']=='true' else False
    videoData['isCrawlable']=True if raw['videoDetails']['isCrawlable'] else False
    videoData['allowRatings']=True if raw['videoDetails']['allowRatings'] else False
    videoData['isPrivate']=True if raw['videoDetails']['isPrivate'] else False
    videoData['isLiveContent']=True if raw['videoDetails']['isLiveContent'] else False
    return videoData
    