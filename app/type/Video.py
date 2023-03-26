import urllib.parse
from urllib.parse import urlparse, parse_qsl

from typing import List, Dict, Union, Any
from enum import Enum
import re
import datetime

from app.type.Base import StrictDictionary

class thumbnail(StrictDictionary):
    url:str
    width:int
    height:int

class strList(list):
    def __init__(self,args:list=list()):
        if not all([isinstance(i, str) for i in args]):
            raise ValueError('keywordList will need to have "str" type items only')
        super().__init__(args)


class dateInt(int):
    
    """
        A subclass of int that stores a date in an integer format that represents 
        the date as the number of milliseconds since the Unix epoch (January 1, 1970).
        
        Accepts date strings in the following formats:
        - 'YYYY-MM-DD'
        - 'YYYY-MM-DDTHH:MM:SSZ'
        - 'YYYY-MM-DDTHH:MM:SS.sssZ'
        - 'YYYY-MM-DDTHH:MM:SS±HH:MM'
        - 'YYYY-MM-DDTHH:MM:SS.sss±HH:MM'
        
        Examples:
        - '2023-03-10'
        - '2023-03-10T14:00:08+00:00'
        - '2023-03-10T14:00:08.999Z'
        - '2023-03-10T14:00:08-07:00'
        - '2023-03-10T14:00:08.999-07:00'
    """
    date_formats = [
        ('%Y-%m-%d', re.compile(r'\d{4}-\d{2}-\d{2}$')),
        ('%Y-%m-%dT%H:%M:%S.%fZ', re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z$')),
        ('%Y-%m-%dT%H:%M:%S.%f%z', re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}$')),
        ('%Y-%m-%dT%H:%M:%SZ', re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$')),
        ('%Y-%m-%dT%H:%M:%S%z', re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}$')),
    ]
    
    def __new__(cls, date_str=None, default_value=-1):
        """
        Creates a new instance of the class with the date_str argument. The argument
        should be a string in one of the accepted datetime formats. The method converts
        the string into a datetime object and then into an integer representing the 
        number of milliseconds since the Unix epoch. The integer is then used to create
        a new instance of the class.
        
        :param date_str: A string representing a date in an accepted datetime format.
        :param default_value: The default value to return if no date string is provided.
        :return: A new instance of the DateInt class.
        """
        if date_str is None:
            return super().__new__(cls, default_value)
        
        # Define accepted datetime formats
        for date_format, regex in cls.date_formats:
            if regex.match(date_str):
                date_obj = datetime.datetime.strptime(date_str, date_format)
                timestamp = int(date_obj.timestamp())
                return super().__new__(cls, timestamp)
        
        raise ValueError("Invalid date string format")

        
    def todatetime(self):
        """
        Converts the internally stored integer timestamp into a datetime object
        and returns it.
        
        :return: A datetime object representing the stored date.
        """
        return datetime.datetime.fromtimestamp(self)

class strbool(int):
    def __new__(cls, value=bool()):
        if isinstance(value, str):
            if value.lower() == "true":
                return super().__new__(cls, 1)
            elif value.lower() == "false":
                return super().__new__(cls, 0)
        return super().__new__(cls, value)


class liveBroadcast(StrictDictionary):
    isLiveNow:strbool
    startTimestamp:dateInt
    endTimestamp:dateInt

class Video(StrictDictionary):
    videoId: str
    title: str
    author: str
    lengthSeconds: str
    keywords: strList
    channelId: str
    shortDescription: str
    viewCount:int
    thumbnail:thumbnail

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
    availableCountries:strList
    liveBroadcastDetails:liveBroadcast
    

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

