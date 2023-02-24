
from enum import Enum
import json

class Loadout:
    pass
class Youtube:
    # This Class is the parent class that will hold all internal data e.g.
    class param:
        def __str__(self) -> str:
            return self.__name__
        def __repr__(self)->str:
            return json.dumps(self.__dict__)
        def __call__(self)->dict:
            return self.__dict__
         
    class next(param):
        def __init__(self, videoId: str = '', continuation: str = '') -> None:
            
            if not videoId and not continuation:
                raise ValueError('Either video_id or continuation must be provided.')
            self.videoId=videoId
            self.continuation=continuation

    
    
class PF(Enum):
        WEB = {
                    "client":  {
                        "clientName": "WEB",
                        "clientVersion": "2.20230213.01.00"
                    }
                }
        
        EMBED = {
                    "client": {
                        "clientName": "WEB_EMBEDDED_PLAYER",
                        "clientVersion": "1.20230131.01.00",
                    }
                }


class VideoManager:
    