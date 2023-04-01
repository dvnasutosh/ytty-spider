
from enum import Enum
from app.dataclass.Base import StrictDictionary
from app.dataclass.common import img,strbool,strList,dateInt,publishTime

class videoMini(StrictDictionary):
    videoId:str
    thumbnail:img
    title:str
    publishedTime:publishTime
    length:int
    viewCount:int
    ownerBadges:bool
    preview:str
    isLatest:bool
class videoMiniList(list):
    def __init__(self,args:list=list()):
        if not all([isinstance(i, videoMini) for i in args]):
            raise ValueError('videoShortList will need to have "videoShort" type items only')
        super().__init__(args)
class sort(Enum):
    popular=0
    latest=1
    default=1
    
class channelVideos(StrictDictionary):
    popularContinuation:str
    latestContinuation:str
    videos:videoMiniList
    videoContinuation:str
    sortBy:sort
    