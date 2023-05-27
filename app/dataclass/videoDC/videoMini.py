
from ast import List
from enum import Enum
from betterdataclass.StrictDictionary import StrictDictionary
from app.dataclass.common import img,strbool,List[str],dateInt,publishTime

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
    

class sort(Enum):
    popular=0
    latest=1
 
class channelVideos(StrictDictionary):
    popularContinuation:str
    latestContinuation:str
    videos:List[videoMini]
    videoContinuation:str
    sortBy:sort
    