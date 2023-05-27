

from typing import List, Literal
from enum import Enum

from betterdataclass.StrictDictionary import StrictDictionary
from app.dataclass.common import img,strbool,dateInt,url


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

class mimeType(Enum):

    unmuxedAudio='unmuxedAudio'
    unmuxedVideo='unmuxedVideo'
    muxedVideo='muxedVideo'
    undefined='undefined'
    default='undefined'

class mimeTypeExt(StrictDictionary):
    Type:Literal['unmuxedAudio','unmuxedVideo','muxedVideo','undefined']
    label:str
    codec:List[str]

class DownloadableMeta(StrictDictionary):
    itag:int
    url:url
    mimeType:mimeTypeExt
    bitrate:int
    lastModified:int
    quality:str
    projectionType:str
    approxDurationMs:int

class videoMeta(StrictDictionary):
    width:int
    height:int
    qualityLabel:str
    fps:int

class audioMeta(StrictDictionary):
    loudnessDb:float
    audioQuality:str
    audioSampleRate:int
    audioChannels:int

class Range(StrictDictionary):
    start:int
    end:int

class adaptiveMeta(StrictDictionary):
    indexRange:Range
    initRange:Range
    contentLength:int
    averageBitrate:int

class streaming(StrictDictionary):
    Download:DownloadableMeta
    videoMeta:videoMeta
    audioMeta:audioMeta


class adaptiveVideo(StrictDictionary):
    Download:DownloadableMeta
    videoMeta:videoMeta
    adaptiveMeta:adaptiveMeta

class adaptiveAudio(StrictDictionary):
    Download:DownloadableMeta
    audioMeta:audioMeta
    adaptiveMeta:adaptiveMeta


class adaptiveList(StrictDictionary):
    audio:List[adaptiveAudio]
    video:List[adaptiveVideo]

class Downloadables(StrictDictionary):
    expiresInSeconds:int
    since:float
    muxed:List[streaming]
    unmuxed:adaptiveList
