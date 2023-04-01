from app.FetchEngine.endpoint import browse
from app.authentication.auth import Authentication
from app.FetchEngine.requests import CONTEXT,PF

from app.DataEngine.deserialise import Deserialise
import time
from json import dumps, loads

from app.dataclass.ChannelDataClasses.params import Params


class channelManager:
    def __init__(self, channelId: str = None, auth: Authentication = Authentication(), context: CONTEXT = CONTEXT()):
        self.auth=auth
        self.context=context

        self.browse = browse(auth=auth, client=context)
        self.params=str()
        self.channelId=str()
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
        channelData=Deserialise.channelHome(raw)
        self.tabs=dict()
        return channelData
    
    def Home(self,channelId:str=str(),params:str=str()):
        channelId=self.channelExists(channelId)
        if not params and not self.params:
            params=self.params=Params.Home
        else: 
            params=self.params
        
        
        raw=loads(self.browse(browseId=channelId,params=params).text)
    
    
    def Videos(self,channelId:str=str(),params:str=str()):
    #     get videoData from channels
        if not params:
            if not self.params:
                self.params=params=Params.Videos.value
            else:
                params=self.params
        
        # Checking whether channelId is given
        channelId=self.channelExists(channelId)
        
        raw=loads(self.browse(browseId=channelId,param=params).text)
        return Deserialise.channelVideo(raw)
    
        
    

"""
    {
        Home
    }
"""