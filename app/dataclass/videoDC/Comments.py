
from app.dataclass.common import img, publishTime
from betterdataclass.StrictDictionary import StrictDictionary
from typing import Union,List


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


class Comments(StrictDictionary):
    count:int
    List:List[Union[Comment,continuationToken]]
