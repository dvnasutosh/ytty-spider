from typing import List, Optional, Union
from app.dataclass.channelDC.Community import Post
from app.dataclass.channelDC.Shelf import ShelfDetails
from app.dataclass.channelDC.about import aboutChannel
from app.dataclass.channelDC.store import Product
from app.dataclass.playlistDC.Playlist import PlaylistMini
from app.dataclass.videoDC.videoMini import videoMini
from betterdataclass.StrictDictionary import StrictDictionary
from betterdataclass.StrictList import StrictList
from app.dataclass.common import img,strbool,browseEndpoint


    
class tabEndpoints(StrictDictionary):
    title:str
    selected:strbool
    browseEndpoint:browseEndpoint

class channelMini(StrictDictionary):
    channelId:str
    title:str
    thumbnail:img
    videoCount:int
    subscriberCount:int
    isVerified:bool    

class Sort(StrictDictionary):
    continuation:str
    isSelected:strbool
    sortType:str
    
class Content(StrictDictionary):
    data: List[Union[videoMini, channelMini, ShelfDetails, Product, Post, PlaylistMini, aboutChannel]]
    sort: Optional[List[Sort]]

class contentList(StrictList): #list
    types= [Content,videoMini, channelMini, ShelfDetails, Product, Post, PlaylistMini, aboutChannel]

    
    

class tabData(StrictDictionary):
    tabs: List[tabEndpoints]
    content: contentList

class Channel(StrictDictionary):
    channelId: str
    title: str
    banner: img
    tvBanner: img
    channelHandle: str
    tagline: str
    subscriberCountApprox: float
    videosCount: int
    description: str
    avatar: img
    availableCountry: List[str]
    
    isFamilySafe: strbool
    isnoindex: strbool
    isunlisted: strbool
    isVerified: bool
    tags: List[str]
    tabs: tabData

