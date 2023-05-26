

# from app.Engines.DataEngine.helper import convert_to_number, filterInt
# from app.dataclass.common import img,strbool,dateInt,url

# from typing import Union
# import time
# import json
# from app.dataclass.videoDC.Comments import Comment, Comments, continuationToken

# from app.dataclass.videoDC.Download import DownloadableMeta, Downloadables, adaptiveAudio, adaptiveMeta, mimeTypeExt, streaming
# from app.dataclass.videoDC.Interactions import Interactions
# from app.dataclass.videoDC.Video import Video, liveBroadcast
from app.Engines.DataEngine.deserialiser.video.details import deserialise_videoDetails
from app.dataclass.videoDC.Video import Video


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

# def deserialise_comment(raw:str):

#     commentRenderer         =   raw['commentThreadRenderer']['comment']['commentRenderer']
    
#     comment=Comment()
    
#     comment.commentId                               =   str(commentRenderer['commentId'])
    
#     for text in commentRenderer['contentText']['runs']:
#         comment.text                                =   str(comment.text + (text['text']+" "))
    
#     comment.author.authorText                       =   str(commentRenderer['authorText']['simpleText'])
#     comment.author.authorThumbnail                  =   img(**commentRenderer['authorThumbnail']['thumbnails'][-1])
#     comment.author.browseId                         =   str(commentRenderer['authorEndpoint']['browseEndpoint']['browseId'])
    
    
#     comment.publishedOn.publishedTimeText           =   str(commentRenderer['publishedTimeText']['runs'][0]['text'])
#     comment.publishedOn.since                       =   float(time.time())
    
#     comment.isLiked                                 =   commentRenderer['isLiked']  == "true"
#     comment.authorIsChannelOwner                    =   commentRenderer['authorIsChannelOwner'] == "true"
    
#     comment.voteStatus                              =   str(commentRenderer['voteStatus'])
#     comment.voteCountApprox                         =   int(convert_to_number(commentRenderer['voteCount']['simpleText']))
#     if 'replies' in raw['commentThreadRenderer'].keys():
#         commentRepliesRenderer  =   raw['commentThreadRenderer']['replies']['commentRepliesRenderer']['contents']

#         comment.replyContinuation                   =   commentRepliesRenderer[0]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
#         comment.replyCount                              =   int(commentRenderer['replyCount'])
#     return comment
    
class Deserialise:
    @staticmethod
    def videoDetails(raw:dict) -> Video:...
    
    
Deserialise.videoDetails=deserialise_videoDetails

    # @staticmethod
    # def interactionData(raw:dict):
    #     interactions=Interactions()
    #     content=raw['contents']['twoColumnWatchNextResults']['results']['results']['contents']
    #     # getting likes
    #     filteredLikeSection=content[0]['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']
    #     # filtering like subtext
    #     likeText=filteredLikeSection['defaultText']['accessibility']['accessibilityData']['label']
        
    #     interactions['likes']                           =       filterInt(likeText)    #Coz f* regex
    #     interactions['comments_continuation']           =       content[3]['itemSectionRenderer']['contents'][0]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
        
    #     return interactions
    
    # @staticmethod
    # def Comments(raw:dict):
    #     CommentList=CommentsList()
        
    #     s=raw['onResponseReceivedEndpoints'][0]['reloadContinuationItemsCommand']['continuationItems'][0]['commentsHeaderRenderer']['countText']['runs'][0]['text']
    #     count=filterInt(s)
    #     Items=raw['onResponseReceivedEndpoints'][1]['reloadContinuationItemsCommand']['continuationItems'][:-1:]
        
    #     for comRaw in Items:
    #         CommentList.append(deserialise_comment(comRaw))
        
    #     #checking For final to be comment or continuation
    #     Items=raw['onResponseReceivedEndpoints'][1]['reloadContinuationItemsCommand']['continuationItems'][-1]
    #     if 'continuationItemRenderer' in Items.keys():
    #         CommentList.append( continuationToken(Items['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token'])    )

    #     elif 'commentThreadRenderer' in Items.keys():
    #         CommentList.append(deserialise_comment(Items))
    #         CommentList.append(continuationToken())
    #     return Comments(count=count,List=CommentList)

    # @staticmethod
    # def ContinuedComments(raw:dict):
    #     CommentList=CommentsList()
    #     Items=raw['onResponseReceivedEndpoints'][0]['appendContinuationItemsAction']['continuationItems']
        
    #     for comRaw in Items[:-1:]:
    #         CommentList.append(deserialise_comment(comRaw))
    #     if 'continuationItemRenderer' in Items[-1].keys():
    #         CommentList.append( continuationToken(Items[-1]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token'])    )

    #     elif 'commentThreadRenderer' in Items[-1].keys():
    #         CommentList.append(deserialise_comment(Items[-1]))
    #         CommentList.append(continuationToken())
    #     return Comments(count=0,List=CommentList)

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
