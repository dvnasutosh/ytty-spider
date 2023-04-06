from typing import List
from app.dataclass.Base import StrictDictionary
from app.dataclass.common import img,strbool,strList
from app.FetchEngine.endpoint import browse

class browseEndpoint(StrictDictionary):
    browseId:str
    params:str
    canonicalBaseUrl:str
    
class tabEndpoints(StrictDictionary):
    title:str
    selected:strbool
    browseEndpoint:browseEndpoint

class tabEndpointsList(list):
    def __init__(self,args:List[tabEndpoints]=list()):
        if not all([isinstance(i, tabEndpoints) for i in args]):
            raise ValueError('tabEndpointsList will need to have "tabEndpoints" type items only')
        super().__init__(args)
    
class tabData(StrictDictionary):
    tabs:tabEndpointsList
    content:list

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

class channelMini(StrictDictionary):
    channelId:str
    title:str
    thumbnail:img
    videoCount:int
    subscriberCount:int
    isVerified:bool    
    
