from typing import Optional
from betterdataclass.StrictDictionary import StrictDictionary
    
class TabRoute(StrictDictionary):
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
            
            