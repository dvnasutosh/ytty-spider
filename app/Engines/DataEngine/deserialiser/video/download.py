
import time
from app.dataclass.videoDC.Download import (
    Downloadables,streaming , DownloadableMeta, adaptiveMeta, adaptiveVideo, adaptiveAudio,
    mimeType, mimeTypeExt
    )
from app.dataclass.common import url
from json import loads

def deserialise_mimeType(mime: str = str()):

        mimeTypeData = mimeTypeExt()
        # Split the input string to extract the mime type and codecs
        parts = mime.split("; ")
        Label = parts[0]
        codecs = parts[1].replace("codecs=\"", "").replace("\"", "")
        
        mimeTypeData.codec = codecs.split(",")
        mimeTypeData.label=Label
        if 'video'in str.lower(Label):
            if mimeTypeData.codec.__len__()==1:
                mimeTypeData.Type=mimeType.unmuxedVideo
            
            elif mimeTypeData.codec.__len__()==2:
                mimeTypeData.Type=mimeType.muxedVideo
            
            else:
                mimeTypeData=mimeType.undefined
        
        elif 'audio' in str.lower(Label):
            mimeTypeData.Type=mimeType.unmuxedAudio
        else:
            mimeTypeData.Type=mimeType.undefined
        return mimeTypeData

def deserialise_streamingData(raw:dict):
        #SECTION: Type Checking For attribute
        try:
            if not isinstance(raw, (str,dict)):
                raise AttributeError('signature given is not of str or dict type')
            
            if isinstance(raw, str):
                raw = loads(raw)

            if not isinstance(raw, (str,dict)):
                raise AttributeError('signature given is not of str or dict type')        
        except Exception():
            raise AttributeError('signature not in proper for mimeType.')
        #!SECTION
        
        DownloadableData=Downloadables()
        
        DownloadableData['expiresInSeconds']=int(raw['streamingData']['expiresInSeconds'])
        DownloadableData['since']=time.time()
        
        for rawItem in raw['streamingData']['formats']:
            streamItem=streaming()
            streamItem.Download.itag                =   int(rawItem['itag'])
            streamItem.Download.url                 =   url(rawItem['url'])
            
            streamItem.Download.mimeType                    =   deserialise_mimeType(mime=rawItem['mimeType'])
            
            streamItem.Download.bitrate                     =   int(rawItem['bitrate'])
            streamItem.Download.lastModified                =   int(rawItem['lastModified'])
            streamItem.Download.quality                     =   str(rawItem['quality'])
            streamItem.Download.projectionType              =   str(rawItem['projectionType'])
            streamItem.Download.approxDurationMs            =   int(rawItem['approxDurationMs'])
            
            streamItem.videoMeta.width                      =   int(rawItem['width'])
            streamItem.videoMeta.height                     =   int(rawItem['height'])
            streamItem.videoMeta.qualityLabel               =   str(rawItem['qualityLabel'])
            streamItem.videoMeta.fps                        =   int(rawItem['fps'])

            streamItem.audioMeta.audioQuality               =   str(rawItem['audioQuality'])
            streamItem.audioMeta.audioSampleRate            =   int(rawItem['audioSampleRate'])
            streamItem.audioMeta.audioChannels              =   int(rawItem['audioChannels'])
            
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
            if commonMeta.mimeType.Type == mimeType.unmuxedAudio:
                adaptiveAudioData               =       adaptiveAudio()
                adaptiveAudioData.Download      =       commonMeta
                adaptiveAudioData.adaptiveMeta  =       adaptive
                
                adaptiveAudioData.audioMeta.audioQuality    =       str(rawItem['audioQuality'])
                adaptiveAudioData.audioMeta.audioSampleRate =       int(rawItem['audioSampleRate'])
                adaptiveAudioData.audioMeta.audioChannels   =       int(rawItem['audioChannels'])
                
                DownloadableData.unmuxed.audio.append(adaptiveAudioData)
            
            elif commonMeta.mimeType.Type == mimeType.unmuxedVideo:
                adaptiveVideoData               =        adaptiveVideo()
                adaptiveVideoData.Download      =       commonMeta
                adaptiveVideoData.adaptiveMeta  =       adaptive
                
                adaptiveVideoData.videoMeta.width           =       int(rawItem['width'])
                adaptiveVideoData.videoMeta.height          =       int(rawItem['height'])
                adaptiveVideoData.videoMeta.qualityLabel    =       str(rawItem['qualityLabel'])
                adaptiveVideoData.videoMeta.fps             =       int(rawItem['fps'])

                DownloadableData.unmuxed.video.append(adaptiveVideoData)
        return DownloadableData
