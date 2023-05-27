

# from app.Engines.DataEngine.helper import convert_to_number, filterInt
# from app.dataclass.common import img,strbool,dateInt,url

# from typing import Union
# import time
# import json
# from app.dataclass.videoDC.Comments import Comment, Comments, continuationToken

# from app.dataclass.videoDC.Download import DownloadableMeta, Downloadables, adaptiveAudio, adaptiveMeta, mimeTypeExt, streaming
# from app.dataclass.videoDC.Interactions import Interactions
# from app.dataclass.videoDC.Video import Video, liveBroadcast
from app.Engines.DataEngine.deserialiser.video.details import (
    deserialise_ContinuedComments, 
    deserialise_comments, 
    deserialise_interactionData, 
    deserialise_videoDetails)
from app.dataclass.videoDC.Video import Interactions, Video
from app.dataclass.videoDC.Comments import Comments


# def deserialise_mimeType(mime: str = str()):

#         mimeType = mimeTypeExt()
#         # Split the input string to extract the mime type and codecs
#         parts = mime.split("; ")
#         Label = parts[0]
#         codecs = parts[1].replace("codecs=\"", "").replace("\"", "")
        
#         mimeType.codec = codecs.split(",")
#         mimeType.label=Label
#         if 'video'in str.lower(Label):
#             if mimeType.codec.__len__()==1:
#                 mimeType.Type=T.unmuxedVideo
            
#             elif mimeType.codec.__len__()==2:
#                 mimeType.Type=T.muxedVideo
            
#             else:
#                 mimeType=T.undefined
        
#         elif 'audio' in str.lower(Label):
#             mimeType.Type=T.unmuxedAudio
#         else:
#             mimeType.Type=T.undefined
#         return mimeType

# 
class Deserialise:
    @staticmethod
    def videoDetails(raw:dict) -> Video:...
    
    @staticmethod
    def interactionData(raw:dict) -> Interactions:...
    
    @staticmethod
    def comments(raw:dict)  -> Comments:...
    
    @staticmethod
    def continuedComments(raw:dict)    -> Comments:...
    
    
Deserialise.videoDetails=deserialise_videoDetails
Deserialise.interactionData=deserialise_interactionData
Deserialise.continuedComments=deserialise_ContinuedComments
Deserialise.comments=deserialise_comments

    


    # @staticmethod
    # def streamingData(raw:dict):
    #     #SECTION: Type Checking For attribute
    #     try:
    #         if not isinstance(raw, (str,dict)):
    #             raise AttributeError('signature given is not of str or dict type')
            
    #         if isinstance(raw, str):
    #             raw = json.loads(raw)

    #         if not isinstance(raw, (str,dict)):
    #             raise AttributeError('signature given is not of str or dict type')        
    #     except Exception():
    #         raise AttributeError('signature not in proper format.')
    #     #!SECTION
        
    #     DownloadableData=Downloadables()
        
    #     DownloadableData['expiresInSeconds']=int(raw['streamingData']['expiresInSeconds'])
    #     DownloadableData['since']=time.time()
        
    #     for rawItem in raw['streamingData']['formats']:
    #         streamItem=streaming()
    #         streamItem.Download.itag                =   int(rawItem['itag'])
    #         streamItem.Download.url                 =   url(rawItem['url'])
            
    #         streamItem.Download.mimeType                    =   deserialise_mimeType(mime=rawItem['mimeType'])
            
    #         streamItem.Download.bitrate                     =   int(rawItem['bitrate'])
    #         streamItem.Download.lastModified                =   int(rawItem['lastModified'])
    #         streamItem.Download.quality                     =   str(rawItem['quality'])
    #         streamItem.Download.projectionType              =   str(rawItem['projectionType'])
    #         streamItem.Download.approxDurationMs            =   int(rawItem['approxDurationMs'])
            
    #         streamItem.videoMeta.width                      =   int(rawItem['width'])
    #         streamItem.videoMeta.height                     =   int(rawItem['height'])
    #         streamItem.videoMeta.qualityLabel               =   str(rawItem['qualityLabel'])
    #         streamItem.videoMeta.fps                        =   int(rawItem['fps'])

    #         streamItem.audioMeta.audioQuality               =   str(rawItem['audioQuality'])
    #         streamItem.audioMeta.audioSampleRate            =   int(rawItem['audioSampleRate'])
    #         streamItem.audioMeta.audioChannels              =   int(rawItem['audioChannels'])
            
    #         DownloadableData.muxed.append(streamItem)
        
    #     for rawItem in raw['streamingData']['adaptiveFormats']:
    #         commonMeta=DownloadableMeta()
    #         adaptive=adaptiveMeta()

    #         commonMeta.itag                                 =       int(rawItem['itag'])
    #         commonMeta.url                                  =       url(rawItem['url'])
    #         commonMeta.mimeType                             =       deserialise_mimeType(mime=rawItem['mimeType'])
    #         commonMeta.bitrate                              =       int(rawItem['bitrate'])
    #         commonMeta.lastModified                         =       int(rawItem['lastModified'])
    #         commonMeta.quality                              =       str(rawItem['quality'])
    #         commonMeta.projectionType                       =       str(rawItem['projectionType'])
    #         commonMeta.approxDurationMs                     =       int(rawItem['approxDurationMs'])

    #         adaptive.averageBitrate                         =       int(rawItem['averageBitrate'])
    #         adaptive.contentLength                          =       int(rawItem['contentLength'])
    #         adaptive.indexRange.start                       =       int(rawItem['initRange']['start'])
    #         adaptive.indexRange.end                         =       int(rawItem['initRange']['end'])
    #         adaptive.indexRange.start                       =       int(rawItem['indexRange']['start'])
    #         adaptive.indexRange.end                         =       int(rawItem['indexRange']['end'])

    #         #   Checking if the data is audio or video data
    #         if commonMeta.mimeType.Type == T.unmuxedAudio:
    #             adaptiveAudioData               =       adaptiveAudio()
    #             adaptiveAudioData.Download      =       commonMeta
    #             adaptiveAudioData.adaptiveMeta  =       adaptive
                
    #             adaptiveAudioData.audioMeta.audioQuality    =       str(rawItem['audioQuality'])
    #             adaptiveAudioData.audioMeta.audioSampleRate =       int(rawItem['audioSampleRate'])
    #             adaptiveAudioData.audioMeta.audioChannels   =       int(rawItem['audioChannels'])
                
    #             DownloadableData.unmuxed.audio.append(adaptiveAudioData)
            
    #         elif commonMeta.mimeType.Type == T.unmuxedVideo:
    #             adaptiveVideoData               =        adaptiveVideo()
    #             adaptiveVideoData.Download      =       commonMeta
    #             adaptiveVideoData.adaptiveMeta  =       adaptive
                
    #             adaptiveVideoData.videoMeta.width           =       int(rawItem['width'])
    #             adaptiveVideoData.videoMeta.height          =       int(rawItem['height'])
    #             adaptiveVideoData.videoMeta.qualityLabel    =       str(rawItem['qualityLabel'])
    #             adaptiveVideoData.videoMeta.fps             =       int(rawItem['fps'])

    #             DownloadableData.unmuxed.video.append(adaptiveVideoData)
    #     return DownloadableData
    
    
    # @staticmethod
    # def channelHome(raw:dict)-> dsl.Channel: ...

    # channelDetails=dsl.deserialise_channelDetails
    # channelVideo=dsl.deserialise_channelVideos
    # channelTabs=dsl.deserialise_Tabs
