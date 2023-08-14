

from enum import Enum
from typing import List


from betterdataclass.StrictDictionary import StrictDictionary

from ..common import url
class mimeType(Enum):

    unmuxedAudio    =   'unmuxedAudio'
    unmuxedVideo    =   'unmuxedVideo'
    muxedVideo      =   'muxedVideo'
    undefined       =   'undefined'
    default         =   'undefined'

class mimeTypeExt(StrictDictionary):
    Type    :mimeType
    label   :str
    codec   :List[str]

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
    Download: DownloadableMeta
    audioMeta: audioMeta
    adaptiveMeta:adaptiveMeta


class adaptiveList(StrictDictionary):
    audio: List[adaptiveAudio]
    video: List[adaptiveVideo]

class Downloadables(StrictDictionary):
    expiresInSeconds: int
    since: float
    muxed: List[streaming]
    unmuxed: adaptiveList
