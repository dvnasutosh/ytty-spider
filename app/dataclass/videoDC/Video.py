

from typing import List


from betterdataclass.StrictDictionary import StrictDictionary
from app.dataclass.common import img,strbool,dateInt


class liveBroadcast(StrictDictionary):
    isLiveNow:strbool
    startTimestamp:dateInt
    endTimestamp:dateInt

class Video(StrictDictionary):
    videoId: str
    title: str
    author: str
    lengthSeconds: str
    keywords: List[str]
    channelId: str
    shortDescription: str
    viewCount:int
    thumbnail:img

    isOwnerViewing: strbool
    isCrawlable: strbool
    allowRatings: strbool
    isPrivate: strbool
    isLiveContent: strbool
    isFamilySafe: strbool

    isUnlisted:strbool
    hasYpcMetadata:strbool
    category:str
    publishDate:dateInt
    uploadDate:dateInt
    availableCountries:List[str]
    liveBroadcastDetails:liveBroadcast

class Interactions(StrictDictionary):
    """stores all interactions relative to a youtube video

    Args:
        StrictDictionary (dict): _description_
    """
    likes:int
    comments_continuation:str


