from Base import DynamicMembers
from typing import Dict, List
import typing

class Video(DynamicMembers):
    videoId:str
    title:str
    author:str
    lengthSeconds:str
    keywords:List[str]
    channelId:str
    shortDescription:str
    video:List[Dict]
    isOnwerViewing:bool
    isCrawlable:bool
    allowRating:bool
    isPrivate:bool
    isLiveContent:bool
