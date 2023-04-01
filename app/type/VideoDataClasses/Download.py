

from enum import Enum

from app.type.Base import StrictDictionary
x
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
