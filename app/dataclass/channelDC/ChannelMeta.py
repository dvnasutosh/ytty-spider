from typing import List, Optional, Union
from app.dataclass.channelDC.Community import Post
from app.dataclass.channelDC.Shelf import ShelfDetails
from app.dataclass.channelDC.about import aboutChannel
from app.dataclass.channelDC.store import Product
from app.dataclass.playlistDC.Playlist import PlaylistMini
from app.dataclass.videoDC.videoMini import videoMini
from betterdataclasses.betterdataclass.StrictDictionary import StrictDictionary
from betterdataclasses.betterdataclass.StrictList import StrictList
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
class dataList(StrictList):
    types=[videoMini, channelMini, ShelfDetails, Product, Post, PlaylistMini, aboutChannel]
class Content(StrictDictionary):
    # data: List[Union[videoMini, channelMini, ShelfDetails, Product, Post, PlaylistMini, aboutChannel]]
    # data: dataList
    data:List
    sort: Optional[List[Sort]]
    
    

class contentList(StrictList): #list
    types= [Content,videoMini, channelMini, ShelfDetails, Product, Post, PlaylistMini, aboutChannel]

# SECTION: Test for List[tabsEndoints] typing type restriction setup being the reason for copy paste list members

class tabEndpointsList(StrictList):
    types=[tabEndpoints]
    
# !SECTION

class tabData(StrictDictionary):
    # tabs: List[tabEndpoints]
    tabs: tabEndpointsList
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

