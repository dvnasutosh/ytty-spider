from typing import List, Union
from betterdataclass.StrictDictionary import StrictDictionary
from betterdataclass.StrictList import StrictList

from app.dataclass.common import img,strbool,List[str]
from app.Engines.FetchEngine.endpoint import browse

class browseEndpoint(StrictDictionary):
    browseId:str
    params:str
    canonicalBaseUrl:str
    
class tabEndpoints(StrictDictionary):
    title:str
    selected:strbool
    browseEndpoint:browseEndpoint

class tabEndpointsList(StrictList):
    types=[tabEndpoints]


class tabData(StrictDictionary):
    tabs:List[tabEndpoints]
    content:List

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
    availableCountry:List[str]
    isFamilySafe:strbool
    isnoindex:strbool
    isunlisted:strbool
    tags:List[str]
    tabs:tabEndpointsList

class channelMini(StrictDictionary):
    channelId:str
    title:str
    thumbnail:img
    videoCount:int
    subscriberCount:int
    isVerified:bool    
    
