from app.type.Base import StrictDictionary
from typing import List, Dict, override

class thumbnail(StrictDictionary):
    url:str
    width:int
    height:int

class keywordList(list):
    def __init__(self,args:list=list()):
        if not all([isinstance(i, str) for i in args]):
            raise ValueError('keywordList will need to have "str" type items only')
        super().__init__(args)


class Video(StrictDictionary):
    videoId: str
    title: str
    author: str
    lengthSeconds: str
    keywords: keywordList
    channelId: str
    shortDescription: str
    viewCount:int
    thumbnail:thumbnail
    isOwnerViewing: bool
    isCrawlable: bool
    allowRatings: bool
    isPrivate: bool
    isLiveContent: bool
    isFamilySafe:bool



    
    
    
    
    
    
    
    
    
    # Test purpose sample Data
# video = Video()
# video['videoId'] = '123456'
# video['title'] = 'My Video Title'
# video['author'] = 'Author Name'
# video['lengthSeconds'] = '600'
# video['keywords'] = ['video', 'content', 'entertainment']
# video['channelId'] = 'ABC123'
# video['shortDescription'] = 'A short description of the video'
# video['video'] = [{'url': 'http://video.com/video1', 'format': 'mp4'}, {'url': 'http://video.com/video2', 'format': 'webm'}]
# video['isOnwerViewing'] = True
# video['isCrawlable'] = False
# video['allowRating'] = True
# video['isPrivate'] = False
# video['isLiveContent'] = False
# print(video)
