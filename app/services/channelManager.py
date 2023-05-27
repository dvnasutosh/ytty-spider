from app.Engines.FetchEngine.endpoint import browse
from app.authentication.auth import Authentication
from app.Engines.FetchEngine.requests import CONTEXT,PF

from app.Engines.DataEngine.deserialise import Deserialise
import time
from json import dumps, loads

from app.dataclass.channelDC.params import Params
from app.dataclass.channelDC.ChannelMeta import browseEndpoint, tabEndpoints


class channelManager:
    
    def __init__(self, channelId: str = None, auth: Authentication = Authentication(), context: CONTEXT = CONTEXT()):
        self.auth=auth
        self.context=context

        self.browse = browse(auth=auth, client=context)
        self.params=str()
        self.channelId = channelId or str()
        

    def updateContext(self, context: CONTEXT):
        self.context=context
        self.browse.UpdateContext(context)

    def channelExists(self,channelId:str):
        if channelId:
            return channelId
        if not self.channelId:
            raise AttributeError('channelId Not set')
        return self.channelId
    
    def Details(self,channelId=str()):
        channelId=self.channelExists(channelId)
        raw=loads(self.browse(browseId=channelId).text)
        channelData=Deserialise.channelHome(raw)
        self.tabs = {}
        return channelData
    
    def Home(self,channelId:str=str(),params:str=str()):
        channelId=self.channelExists(channelId)
        if not params and not self.params:
            params=self.params=Params.Home
        else: 
            params=self.params
        
        
        raw=loads(self.browse(browseId=channelId,params=params).text)

    def Videos(self,channelId:str=str(),params:str=str()):
        if not params:
            if self.params:
                params=self.params

            else:
                self.params=params=Params.Videos.value
        # Checking whether channelId is given
        channelId=self.channelExists(channelId)

        raw=loads(self.browse(browseId=channelId,param=params).text)
        Details=Deserialise.channelDetails(raw)
        Tabs=Deserialise.channelTabs(raw)


        return Deserialise.channelVideo(raw)
    
    def Shorts(self,channelId:str=str(),params:str=str()):
        if not params:
            if self.params:
                params=self.params
            else:
                self.params=params=Params.Shorts.value
        
    def Tab(self, browse:browseEndpoint):
        raw=loads(self.browse(**browse.__raw__()).text)
        channelDetails=Deserialise.channelDetails(raw)
        channelTabs=Deserialise.channelTabs(raw)
        return channelTabs
        
    

"""
    {
        Home
    }
"""