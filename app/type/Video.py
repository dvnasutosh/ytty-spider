import urllib.parse
from urllib.parse import urlparse, parse_qsl

from typing import List, Dict, Union, Any
from enum import Enum
import re

from app.type.Base import StrictDictionary

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

class mimeType(Enum):

    unmuxedAudio='unmuxedAudio'
    unmuxedVideo='unmuxedVideo'
    muxedVideo='muxedVideo'
    undefined='undefined'
    default='undefined'

class mimeTypeExt(StrictDictionary):
    Type:mimeType
    label:str
    codec:List[str]

class url(str):
    def __new__(cls, url_string=str()):
        if not url_string:
            obj=super().__new__(cls,url_string)
            obj.query_params=dict()
            return obj
        if not isinstance(url_string, str):
            raise TypeError(f"Expected str, but got {type(string).__name__}")
        parsed_url = urlparse(url_string)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError("Invalid URL")
        obj = super().__new__(cls, url_string)
        obj.query_params = dict(parse_qsl(parsed_url.query))
        return obj

    @staticmethod
    def is_valid_url(url_string):
        regex = re.compile(
            r"^(?:http|ftp)s?://"  # http:// or https:// or ftp:// or ftps://
            # domain...
            r"(?:[A-Za-z0-9]+(?:[-._][A-Za-z0-9]+)*\.)+[A-Za-z]{2,}"
            # port...
            r"(?::\d{2,5})?"
            # path...
            r"(?:/.*)?$",
            re.IGNORECASE
        )

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

class streamingList(list):
    def __init__(self,args:list=list()):
        if not all([isinstance(i, streaming) for i in args]):
            raise ValueError('streamingList will need to have "streaming" type items only')
        super().__init__(args)

class adaptiveVideo(StrictDictionary):
    Download:DownloadableMeta
    videoMeta:videoMeta
    adaptiveMeta:adaptiveMeta

class adaptiveVideoList(list):
    def __init__(self,args:list=list()):
        if not all([isinstance(i, adaptiveVideo) for i in args]):
            raise ValueError('adaptiveVideoList will need to have "adaptiveVideo" type items only')
        super().__init__(args)

class adaptiveAudio(StrictDictionary):
    Download:DownloadableMeta
    audioMeta:audioMeta
    adaptiveMeta:adaptiveMeta

class adaptiveAudioList(list):
    def __init__(self,args:list=list()):
        if not all([isinstance(i, adaptiveAudio) for i in args]):
            raise ValueError('adaptiveAudioList will need to have "adaptiveAudio" type items only')
        super().__init__(args)


class adaptiveList(StrictDictionary):
    audio:adaptiveAudioList
    video:adaptiveVideoList

class Downloadables(StrictDictionary):
    expiresInSeconds:int
    since:float
    muxed:streamingList
    unmuxed:adaptiveList

