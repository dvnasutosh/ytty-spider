from typing import Optional
from betterdataclasses.betterdataclass.StrictDictionary import StrictDictionary
    
class TabRoute(StrictDictionary):
    """ API call Validation of Tab route of channel
    
    Extends: 
        `StrictDictionary`
    
    Args:
        `params`: str
        `channelId`: str
        
    """ 
    params:str
    channelId:str    

class Validate:
    # Validation Purpose
    class video:
        class Details(StrictDictionary):
            videoId:str
        class Comments(StrictDictionary):
            videoId:Optional[str]
            continuation:Optional[str]
    class Common:
        class Options(StrictDictionary):
            hl:str
            gl:str
            
            