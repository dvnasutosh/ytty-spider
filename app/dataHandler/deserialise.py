
from app.type.Video import Video,thumbnail,keywordList

from app.type.Video import streaming, DownloadableMeta,Downloadables

from app.type.Video import adaptiveAudio, adaptiveVideo,adaptiveMeta

from app.type.Video import mimeTypeExt,url,mimeType as T



from app.type.Interactions import Interactions

from typing import Union
import time
import json

def deserialise_mimeType(mime: str = str()):
        
        mimeType = mimeTypeExt()
        # Split the input string to extract the mime type and codecs
        parts = mime.split("; ")
        Label = parts[0]
        codecs = parts[1].replace("codecs=\"", "").replace("\"", "")
        
        mimeType.codec = codecs.split(",")
        mimeType.label=Label
        if 'video'in str.lower(Label):
            if mimeType.codec.__len__()==1:
                mimeType.Type=T.unmuxedVideo
            
            elif mimeType.codec.__len__()==2:
                mimeType.Type=T.muxedVideo
            
            else:
                mimeType=T.undefined
        
        elif 'audio' in str.lower(Label):
            mimeType.Type=T.unmuxedAudio
        else:
            mimeType.Type=T.undefined
        return mimeType

class Deserialise:
    @staticmethod
    def videoData(raw:dict) -> dict:
        # videoData=Video()
        videoData=Video()
            
        videoData['videoId']            =   raw['videoDetails']['videoId']
        videoData['title']              =   raw['videoDetails']['title']
        videoData['author']             =   raw['videoDetails']['author']
        videoData['lengthSeconds']      =   raw['videoDetails']['lengthSeconds']
        videoData['keywords']           =   keywordList(args=raw['videoDetails']['keywords']) if 'keywords' in raw['videoDetails'].keys() else keywordList()
        videoData['channelId']          =   raw['videoDetails']['channelId']
        videoData['shortDescription']   =   raw['videoDetails']['shortDescription']
        videoData['viewCount']          =   int(raw['videoDetails']['viewCount'])

        videoData['thumbnail']          =   thumbnail(**raw['videoDetails']['thumbnail']['thumbnails'][-1])
        
        videoData['isOwnerViewing']     =   True if raw['videoDetails']['isOwnerViewing']=='true' else False
        videoData['isCrawlable']        =   True if raw['videoDetails']['isCrawlable'] else False
        videoData['allowRatings']       =   True if raw['videoDetails']['allowRatings'] else False
        videoData['isPrivate']          =   True if raw['videoDetails']['isPrivate'] else False
        videoData['isLiveContent']      =   True if raw['videoDetails']['isLiveContent'] else False
        return videoData
    
    @staticmethod
    def interactionData(raw:dict):
        interactions=Interactions()
        content=raw['contents']['twoColumnWatchNextResults']['results']['results']['contents']
        # getting likes
        filteredLikeSection=content[0]['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']
        # filtering like subtext
        likeText=filteredLikeSection['defaultText']['accessibility']['accessibilityData']['label']
        
        interactions['likes']                           =       int(''.join([i for i in likeText if str.isdigit(i)]))    #Coz f* regex
        interactions['comments_continuation']           =       content[3]['itemSectionRenderer']['contents'][0]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
        
        return interactions
    
    @staticmethod
    def streamingData(raw:dict):
        #SECTION: Type Checking For attribute
        try:
            if not isinstance(raw, (str,dict)):
                raise AttributeError('signature given is not of str or dict type')
            
            if isinstance(raw, str):
                raw = json.loads(raw)

            if not isinstance(raw, (str,dict)):
                raise AttributeError('signature given is not of str or dict type')        
        except Exception():
            raise AttributeError('signature not in proper format.')
        #!SECTION
        
        DownloadableData=Downloadables()
        
        DownloadableData['expiresInSeconds']=int(raw['streamingData']['expiresInSeconds'])
        DownloadableData['since']=time.time()
        
        for rawItem in raw['streamingData']['formats']:
            streamItem=streaming()
            streamItem.Download.itag                =   int(rawItem['itag'])
            streamItem.Download.url                 =   url(rawItem['url'])
            
            streamItem.Download.mimeType            =   deserialise_mimeType(mime=rawItem['mimeType'])
            
            streamItem.Download.bitrate             =   int(rawItem['bitrate'])
            streamItem.Download.lastModified        =   int(rawItem['lastModified'])
            streamItem.Download.quality             =   str(rawItem['quality'])
            streamItem.Download.projectionType      =   str(rawItem['projectionType'])
            streamItem.Download.approxDurationMs    =   int(rawItem['approxDurationMs'])
            
            streamItem.videoMeta.width              =   int(rawItem['width'])
            streamItem.videoMeta.height             =   int(rawItem['height'])
            streamItem.videoMeta.qualityLabel       =   str(rawItem['qualityLabel'])
            streamItem.videoMeta.fps                =   int(rawItem['fps'])

            streamItem.audioMeta.audioQuality       =   str(rawItem['audioQuality'])
            streamItem.audioMeta.audioSampleRate    =   int(rawItem['audioSampleRate'])
            streamItem.audioMeta.audioChannels      =   int(rawItem['audioChannels'])
            
            DownloadableData.muxed.append(streamItem)
        
        for rawItem in raw['streamingData']['adaptiveFormats']:
            commonMeta=DownloadableMeta()
            adaptive=adaptiveMeta()

            commonMeta.itag                                 =       int(rawItem['itag'])
            commonMeta.url                                  =       url(rawItem['url'])
            commonMeta.mimeType                             =       deserialise_mimeType(mime=rawItem['mimeType'])
            commonMeta.bitrate                              =       int(rawItem['bitrate'])
            commonMeta.lastModified                         =       int(rawItem['lastModified'])
            commonMeta.quality                              =       str(rawItem['quality'])
            commonMeta.projectionType                       =       str(rawItem['projectionType'])
            commonMeta.approxDurationMs                     =       int(rawItem['approxDurationMs'])

            adaptive.averageBitrate                         =       int(rawItem['averageBitrate'])
            adaptive.contentLength                          =       int(rawItem['contentLength'])
            adaptive.indexRange.start                       =       int(rawItem['initRange']['start'])
            adaptive.indexRange.end                         =       int(rawItem['initRange']['end'])
            adaptive.indexRange.start                       =       int(rawItem['indexRange']['start'])
            adaptive.indexRange.end                         =       int(rawItem['indexRange']['end'])

            #   Checking if the data is audio or video data
            if commonMeta.mimeType.Type == T.unmuxedAudio:
                adaptiveAudioData               =       adaptiveAudio()
                adaptiveAudioData.Download      =       commonMeta
                adaptiveAudioData.adaptiveMeta  =       adaptive
                
                adaptiveAudioData.audioMeta.audioQuality    =       str(rawItem['audioQuality'])
                adaptiveAudioData.audioMeta.audioSampleRate =       int(rawItem['audioSampleRate'])
                adaptiveAudioData.audioMeta.audioChannels   =       int(rawItem['audioChannels'])
                
                DownloadableData.unmuxed.audio.append(adaptiveAudioData)
            
            elif commonMeta.mimeType.Type == T.unmuxedVideo:
                adaptiveVideoData               =        adaptiveVideo()
                adaptiveVideoData.Download      =       commonMeta
                adaptiveVideoData.adaptiveMeta  =       adaptive
                
                adaptiveVideoData.videoMeta.width           =       int(rawItem['width'])
                adaptiveVideoData.videoMeta.height          =       int(rawItem['height'])
                adaptiveVideoData.videoMeta.qualityLabel    =       str(rawItem['qualityLabel'])
                adaptiveVideoData.videoMeta.fps             =       int(rawItem['fps'])

                DownloadableData.unmuxed.video.append(adaptiveVideoData)
        # Testing
        # print(raw['streamingData']['formats'])
        # print(raw['streamingData']['adaptiveFormats'])
        # print(DownloadableData(raw=True))

        return DownloadableData