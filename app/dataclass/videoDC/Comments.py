
from app.dataclass.common import img, publishTime, strbool
from betterdataclasses.betterdataclass.StrictDictionary import StrictDictionary
from typing import Dict, Optional, Union,List


class authorSimple(StrictDictionary):
    authorText:str
    authorThumbnail:img
    browseId:str


class Comment(StrictDictionary):
    commentId:str
    text:str
    author:authorSimple
    publishedOn:publishTime
    replyCount:int
    isLiked:bool
    replyContinuation:str
    authorIsChannelOwner:bool
    voteStatus:str
    voteCountApprox:int

class continuationToken(str):
    def __new__(cls,data=str()):
        return super().__new__(cls,data)


class SortMember(StrictDictionary):
    name:str
    continuation:continuationToken
    selected:strbool
    
class Comments(StrictDictionary):
    sortBy: Optional[List[SortMember]]
    count: Optional[int]
    Listed: List[Union[Comment,continuationToken]]
