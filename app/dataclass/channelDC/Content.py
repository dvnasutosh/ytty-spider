from typing import List, Union, Optional
from app.dataclass.channelDC.ChannelMeta import channelMini
from app.dataclass.channelDC.Community import Post
from app.dataclass.channelDC.Shelf import ShelfDetails
from app.dataclass.channelDC.about import aboutChannel
from app.dataclass.channelDC.store import Product
from app.dataclass.playlistDC.Playlist import PlaylistMini
from app.dataclass.videoDC.videoMini import videoMini
from betterdataclasses.betterdataclass.StrictDictionary import StrictDictionary 

from enum import Enum

from app.dataclass.common import strbool

class ContentType(Enum):
    channel=channelMini
    video=videoMini
    playlist=PlaylistMini
    product=Product
    post=Post
    about=aboutChannel
    shelf=ShelfDetails
    
    default=None



# The class defines a content object that contains data and a sort object for sorting the data.
# class Sort(StrictDictionary):
#     continuation:str
#     isSelected:strbool
#     sortType:str
    
# class Content(StrictDictionary):
#     data:List[Union[videoMini, channelMini, ShelfDetails, Product, Post, PlaylistMini, aboutChannel]]
#     sort:Sort

