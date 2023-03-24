from app.type.Base import StrictDictionary
from app.type.Video import thumbnail


class authorSimple(StrictDictionary):
    authorText:str
    authorThumbnail:thumbnail
    browseId:str
class publishTime(StrictDictionary):
    publishedTimeText:str
    since:float

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

class CommentsList(list):
    def __init__(self,args:list=list()):
        if not all([isinstance(i, (Comment,continuationToken)) for i in args]):
            raise ValueError('adaptiveVideoList will need to have "adaptiveVideo" type items only')
        super().__init__(args)


class Comments(StrictDictionary):
    count:int
    List:CommentsList
