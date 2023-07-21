from json import loads, dumps
import time


from app.Engines.DataEngine.deserialise import Deserialise
from app.Engines.DataEngine.deserialiser.video.download import insert_url
from app.Engines.FetchEngine.endpoint import player, next
from app.Engines.FetchEngine.requests import CONTEXT, PF

from app.authentication.auth import Authentication
from pytube import YouTube

class videoManager:
    def __init__(self, videoId: str = None, auth: Authentication = Authentication(), context: CONTEXT = CONTEXT()):
        self.auth = auth
        self.context = context

        self.next = next(auth=auth, client=context)
        self.player = player(auth=auth, client=context)

        if videoId:
            self.videoId = videoId

    def updateContext(self, context: CONTEXT):
        self.context = context
        self.next.UpdateContext(context)
        self.player.UpdateContext(context)

    def videoExists(self, videoId: str):

        if videoId:
            return videoId
        if not self.videoId:
            raise AttributeError('videoId Not set')
        return self.videoId

    def setvideoId(self, videoId: str):
        self.videoId = videoId

    def Details(self, videoId: str = str()):
        """
        Returns video Details. 
        """
        videoId = self.videoExists(videoId)

        return Deserialise.videoDetails(loads(self.player(videoId).text))

    def interactionData(self, videoId: str = str()):
        """
        - Returns: `Interaction` Details
        """
        videoId = self.videoExists(videoId)

        return Deserialise.interactionData(loads(self.next(videoId).text))

    def comments(self, videoId: str = str(), continuation: str = str(), continued=bool()):
        
        if not continuation:
            videoId = self.videoExists(videoId)
            continuation = self.interactionData(videoId).comments_continuation

        self.next.UpdatePF(PF.WEB)

        raw = self.next(videoId=videoId, continuation=continuation)

        if continued or (loads(raw.text)['onResponseReceivedEndpoints'].__len__() == 1):
            return Deserialise.ContinuedComments(loads(raw.text))
        else:
            return Deserialise.comments(loads(raw.text))

    def Download(self,videoId:str=str()):

        videoId=self.videoExists(videoId)

        downloadRequest=player(self.auth,self.context)

        #   Initial Requests
        downloadRequest.UpdatePF(PF.WEB)
        raw=loads(downloadRequest(videoId).content)

        #   Handling 'LOGIN REQUIRED' friends
        if raw['playabilityStatus']['status']=='LOGIN_REQUIRED':
            downloadRequest.UpdatePF(PF.TV)

            raw=loads(downloadRequest(videoId).content)

        #   Handling CipherError and all other error
        if raw['playabilityStatus']['status']!='OK' or 'signatureCipher' in raw['streamingData']['formats'][0].keys():
            print('hello2222')
            return insert_url(
                pytubeData=YouTube(f'https://www.youtube.com/watch?v={videoId}').streaming_data,
                structuredData=Deserialise.streamingData(raw))
        
        # Extracting Data
        return Deserialise.streamingData(raw)
    
"""

Sample videoIds
rXMX4YJ7Lks -> Age restricted Data
"""
