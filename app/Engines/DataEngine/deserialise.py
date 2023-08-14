

# from app.Engines.DataEngine.helper import convert_to_number, filterInt
# from app.dataclass.common import img,strbool,dateInt,url

# from typing import Union
# import time
# import json
# from app.dataclass.videoDC.Comments import Comment, Comments, continuationToken

# from app.dataclass.videoDC.Download import DownloadableMeta, Downloadables, adaptiveAudio, adaptiveMeta, mimeTypeExt, streaming
# from app.dataclass.videoDC.Interactions import Interactions
# from app.dataclass.videoDC.Video import Video, liveBroadcast
from app.Engines.DataEngine.deserialiser.channelData import deserialise_Tabs, deserialise_channelDetails
from app.Engines.DataEngine.deserialiser.video.details import (
    deserialise_ContinuedComments, 
    deserialise_comments, 
    deserialise_interactionData, 
    deserialise_videoDetails)
from app.Engines.DataEngine.deserialiser.video.download import deserialise_streamingData
from app.dataclass.channelDC.ChannelMeta import Channel, tabData, tabEndpoints
from app.dataclass.videoDC.Download import Downloadables
from app.dataclass.videoDC.Video import Interactions, Video
from app.dataclass.videoDC.Comments import Comments


class Deserialise:
    @staticmethod
    def videoDetails(raw:dict) -> Video:...
    
    @staticmethod
    def interactionData(raw:dict) -> Interactions:...
    
    @staticmethod
    def comments(raw:dict)  -> Comments:...
    
    @staticmethod
    def continuedComments(raw:dict)    -> Comments:...
    
    @staticmethod
    def streamingData(raw:dict)         ->Downloadables:...
    
    # Channel Related
    @staticmethod
    def channelDetails(raw:dict)        ->Channel:...
    
    @staticmethod
    def channelTabs(raw:dict)              ->tabData:...

Deserialise.videoDetails            =   deserialise_videoDetails
Deserialise.interactionData         =   deserialise_interactionData
Deserialise.continuedComments       =   deserialise_ContinuedComments
Deserialise.comments                =   deserialise_comments
Deserialise.streamingData           =   deserialise_streamingData

Deserialise.channelDetails=deserialise_channelDetails
Deserialise.channelTabs=deserialise_Tabs

    # @staticmethod

    
    
    # @staticmethod
    # def channelHome(raw:dict)-> dsl.Channel: ...

    # channelDetails=dsl.deserialise_channelDetails
    # channelVideo=dsl.deserialise_channelVideos
    # channelTabs=dsl.deserialise_Tabs
