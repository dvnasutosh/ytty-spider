from enum import Enum
from urllib.parse import urlencode


# URL.py
class ResourceName(Enum):
    API:str=r'https://www.youtube.com/'

class Route:
    route_path='youtubei/v1/'
    class Endpoint:
        PLAYER:str='player'
        NEXT:str='next'
        BROWSE:str='browse'
        GUIDE:str='guide'
        SEARCH:str='search'
    def __init__(self,ROUTE) -> None:
        self.__path=self.route_path+getattr(self.Endpoint,ROUTE)
    def __repr__(self) -> str:
        return self.__path
class queryString:
    basic={'key':'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'}

class URL:
    def __init__(self,Endpoint:Route.Endpoint) -> None:
         self.__data=ResourceName.API+Route(Endpoint)+"?"+urlencode(queryString.basic)
    def __repr__(self) -> str:
        return self.__data
    
    
    
# payload.py
class PF:
    EMBED={
    "client": {
        "clientName": "WEB_EMBEDDED_PLAYER",
        "clientVersion": "1.20230131.01.00",
    }}
    WEB={
        "client": {
            "clientName": "WEB",
            "clientVersion": "2.20230213.01.00"
        }
    }


class payload:
    def __init__(self,PF:PF) -> None:
        pass

    
class Params(Enum):
    
    pass

class OPTIONS:
     def __init__(self,PF:PF,) -> None:
          pass

class YTAPI:
    
    def __init__(self,) -> None:
        pass         
    def setupAPI()->None:
        pass
