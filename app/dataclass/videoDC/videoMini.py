
from typing import List, Optional
from enum import Enum
from betterdataclasses.betterdataclass.StrictDictionary import StrictDictionary
from app.dataclass.common import  img, publishTime, publishTime

class videoMini(StrictDictionary):
    videoId:str
    thumbnail:Optional[img]
    title:str
    publishedTime:publishTime
    length:Optional[int]
    viewCount:int
    ownerBadges:bool
    preview:Optional[str]
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
