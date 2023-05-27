from app.dataclass.ChannelDataClasses.params import Params
from app.services.channelManager import channelManager

def Home(self:channelManager,channelId:str=str(),params:str=str()):
    
    channelId=self.channelExists(channelId)
    if not params and not self.params:
        params=self.params=Params.Home
    else: 
        params=self.params 
            
    
