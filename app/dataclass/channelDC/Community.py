from app.dataclass.common import img, publishTime
from app.dataclass.ChannelDataClasses.ChannelMeta import browseEndpoint
from betterdataclass.StrictDictionary import StrictDictionary,StrictList
from app.dataclass.VideoDataClasses.videoMini import sort, videoMini

class Choice(StrictDictionary):
    label:str
    voteCount:int
    selected:bool
    votePercentage:int
    voteRatio:float
    voteRatioIfNotSelected:float
    voteRatioIfSelected:float
    selectActionEndpoint:str
    deselectActionEndpoint:str
    
class Choices(StrictList):
    types=[Choice]
    sortBy=sort
class Poll(StrictDictionary):
    totalVotesApprox:int
    choices:Choices
    

class Post(StrictDictionary):
    postId:str
    authorEndpoint:browseEndpoint
    authorThumbnail:img
    content:str
    publishedTimeText:publishTime
    
    voteStatus:str
    voteCount:int
    
    commentCountApprox:int
    commentEndpoint:browseEndpoint
    
    image:img
    poll:Poll
    video:videoMini
