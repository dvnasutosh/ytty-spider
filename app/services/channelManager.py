from typing import Union
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
        raw=loads(self.browse(browseId=channelId,params=Params.About).text)
        channelData=Deserialise.channelTabs(raw)
        self.tabs = {}
        return channelData
    
    def Tabs(self,browseID:str=str(),params: Union[str,Params]=''):
        
        browseID=self.channelExists(browseID)
        raw=loads(self.browse(browseId=browseID,params=params).text)
        channelDetails=Deserialise.channelDetails(raw)
        channelTabs=Deserialise.channelTabs(raw)

        return {
                'channelDetails': channelDetails.__raw__(),
                'tabData': channelTabs.__raw__()
            }
