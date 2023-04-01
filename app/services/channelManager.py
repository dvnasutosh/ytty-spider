from app.fetchHandler.endpoint import browse
from app.authentication.auth import Authentication
from app.fetchHandler.requests import CONTEXT,PF

from app.dataHandler.deserialiser.channelData import deserialise_channelDetails
from app.dataHandler.deserialise import Deserialise

from json import loads,dumps
import time

class channelManager:
    def __init__(self, channelId: str = None, auth: Authentication = Authentication(), context: CONTEXT = CONTEXT()):
        self.auth=auth
        self.context=context

        self.browse = browse(auth=auth, client=context)

        if channelId:
            self.channelId = channelId
        
    
    def updateContext(self, context: CONTEXT):
        self.context=context
        self.browse.UpdateContext(context)

    def channelExists(self,channelId:str):
        if not channelId:
            if not self.channelId:
                raise AttributeError('channelId Not set')
            return self.channelId
        else:
            return channelId
    
    def Details(self,channelId=str()):
        channelId=self.channelExists(channelId)
        raw=loads(self.browse(browseId=channelId).text)
        channelData-Deserialise.channelHome(raw)
        self.tabs=dict()
        return channelDa
    def Home(self,channelId:str=str(),params:str=str()):
        channelId=self.channelExists(channelId)
        if not params:
            if not self.params:
                raise AttributeError(' `params` not found')
            else: 
                params=self.params
        
        
        raw=loads(self.browse(browseId=channelId,params=params).text)
        

"""
    {
        Home
    }
"""