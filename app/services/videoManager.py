from json import loads,dumps
import time

from app.authentication.auth import Authentication
from app.fetchHandler.endpoint import next, player
from app.fetchHandler.requests import CONTEXT,PF

from app.dataHandler.deserialise import Deserialise



class videoManager:
    def __init__(self, videoId: str = None, auth: Authentication = Authentication(), context: CONTEXT = CONTEXT()):
        self.videoId = videoId
        self.auth=auth
        self.context=context

        self.next = next(auth=auth, client=context)
        self.player = player(auth=auth, client=context)
        if videoId:
            self.details = self.fetchDetails(videoId)
    
    def updateContext(self, context: CONTEXT):
        self.context=context
        self.next.UpdateContext(context)
        self.player.UpdateContext(context)

    def fetchDetails(self, videoId: str):
        return Deserialise.videoData(loads(self.player(videoId).text))
        # return loads(self.player(videoId).text)
    
    def setvideoId(self,videoId:str):
        self.videoId=videoId

    def Download(self,videoId:str=str()):
        if not videoId:
            if not self.videoId:
                raise AttributeError('videoId Not set')
            videoId=self.videoId
        downloadRequest=player(self.auth,self.context)
        
        #   Initial Requests
        downloadRequest.UpdatePF(PF.ANDROID)
        raw=loads(downloadRequest(videoId).content)

        #   Handling 'LOGIN REQUIRED friends
        if raw['playabilityStatus']['status']=='LOGIN_REQUIRED':
            downloadRequest.UpdatePF(PF.TV)
            raw=loads(downloadRequest(videoId).content)
        if raw['playabilityStatus']['status']!='OK':
            raise RuntimeError(f"Seems like there is a problem with youtube restriction in sending mp4 and mp4a data\n {raw['playabilityStatus']}")


        #   Handling CipherError
        if 'signatureCipher' in raw['streamingData']['formats'][0].keys():
            return 'cipheredData:Deciphering To be Implemented'
        
        # Extracting Data

        return Deserialise.streamingData(raw) 

"""
Sample videoIds
rXMX4YJ7Lks -> Age restricted Data
"""