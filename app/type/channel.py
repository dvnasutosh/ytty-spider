from app.type.Base import StrictDictionary
from app.type.common import img,strbool,strList

class tabEndpoints(StrictDictionary):
    title:str
    selected:strbool
    params:str

class tabEndpointsList(list):
    def __init__(self,args:list=list()):
        if not all([isinstance(i, tabEndpoints) for i in args]):
            raise ValueError('tabEndpointsList will need to have "tabEndpoints" type items only')
        super().__init__(args)

class Channel(StrictDictionary):
    channelId:str
    title:str
    banner:img
    tvBanner:img
    channelHandle:str
    tagline:str
    subscriberCountApprox:float
    videosCount:int
    description:str
    avatar:img
    availableCountry:strList
    isFamilySafe:strbool
    isnoindex:strbool
    isunlisted:strbool
    tags:strList
    tabs:tabEndpointsList
    