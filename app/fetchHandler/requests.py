from urllib.parse import urlencode
import requests
from typing import Any
import json
from enum import Enum
class ResourceName(Enum):
    API:str=r'https://www.youtube.com/'
    # SHint:str=r'https://suggestqueries-clients6.youtube.com/'
class Route:
    route_path=r'youtubei/v1/'
    # SHint=r'complete/'    TODO: Adding a separate pathway for search hinting
    def __init__(self,ROUTE) -> None:
        self.__path=self.route_path+getattr(self.Endpoint,ROUTE)
    def __repr__(self) -> str:
        return self.__path
class queryString:
    basic={'key':'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'}
    # searchQuery=dict({
    #     'client':'youtube',
    #     'q':None})
    
class URL:
    def __init__(self,Endpoint:str) -> None:
         self.__data=ResourceName.API
         +Route(Endpoint)
         +"?"
         +urlencode(queryString.basic)
         
    def __repr__(self) -> str:
        return self.__data
    
class Header:
    def __init__(self,Auth=None) -> None:
        if not Auth:
            self.header=None

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


class Payload:
    def __init__(self,Uparam:dict,PF:PF=PF.WEB,geoLocation='in') -> None:
        self._data={'context':PF}
        self._data['context']['gl']=geoLocation
        for i, j in Uparam:
            self._data[i]=j
    def __repr__(self) -> str:
        return json.dumps(self._data)
    def __call__(self) -> dict:
        self._data
    

class yt_requests:
    def __init__(self):
        self.URL:URL
        self.PAYLOAD:Payload
        self.Header:Header

    def __init_subclass__(cls) -> None:
        if not issubclass(cls,Endpoint_Base):
            raise TypeError('doesn\'t inherit Endpoint_Base')
        
        cls.URL=URL(cls.__name__)
        cls.PAYLOAD=Payload(Uparam=cls(),PF=cls.PF)
        cls.Header=Header()
    def Fetch(self):
        return requests.Request(url=self.URL,data=self.PAYLOAD,headers=self.Header)


class endpoint_base:
    def __init__(self) -> None:
        self.PF:PF=PF.WEB
        self.gl:PF='In'
    def __str__(self) -> str:
        return self.__name__
    def __repr__(self)->str:
        return json.dumps(self.__dict__)
    def __call__(self)->dict:
        return self.__dict__
      