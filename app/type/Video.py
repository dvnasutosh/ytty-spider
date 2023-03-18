import urllib.parse
from app.type.Base import StrictDictionary
from typing import List, Dict, Union, Any
from enum import Enum

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

class url:
    def __init__(self,data=''):
        self.raw=str(data)
    def __repr__(self):
        return self.raw


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

print(isinstance(adaptiveVideo, adaptiveAudio))