
from app.type.Base import StrictDictionary
from app.type.common import img,strbool,strList,dateInt,publishTime

class videoTiny(StrictDictionary):
    videoId:str
    thumbnail:img
    title:str
    accessibilityData:str
    publishedTime:publishTime
    lengthText:int
    viewCount:int
    ownerBadges:bool

class videoShortList(list):
    def __init__(self,args:list=list()):
        if not all([isinstance(i, videoShort) for i in args]):
            raise ValueError('videoShortList will need to have "videoShort" type items only')
        super().__init__(args)

class channelVideos(StrictDictionary):
    pass