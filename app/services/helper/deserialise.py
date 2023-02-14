from app.type.Video import Video

def deserialise_videoData(raw:dict):
    videoData=Video()
        
    videoData['videoId']=raw['videoDetails']['videoId']
    videoData['title']=raw['videoDetails']['title']
    videoData['author']=raw['videoDetails']['title']
    videoData['lengthSeconds']=raw['videoDetails']['lengthSeconds']
    videoData['keywords']=raw['videoDetails']['keywords']
    videoData['channelId']=raw['videoDetails']['channelId']
    videoData['shortDescription']=raw['videoDetails']['shortDescription']
    videoData['thumbnail']=raw['videoDetails']['thumbnail']['thumbnails']
    
    videoData['isOwnerViewing']=True if raw['videoDetails']['isOwnerViewing']=='true' else False
    videoData['isCrawlable']=True if raw['videoDetails']['isCrawlable'] else False
    videoData['allowRatings']=True if raw['videoDetails']['allowRatings'] else False
    videoData['isPrivate']=True if raw['videoDetails']['isPrivate'] else False
    videoData['isLiveContent']=True if raw['videoDetails']['isLiveContent'] else False
    return videoData
    