from urllib.parse import urlencode
import requests
from typing import Any

    
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
         self.__data=ResourceName.API+Route(Endpoint)+"?"+urlencode(queryString.basic)
    def __repr__(self) -> str:
        return self.__data
    
class Header:
    def __init__(self,Auth=None) -> None:
        if not Auth:
            self.header=None


class Requests:
    def __init__(self,API:object):
        self.URL=URL(API.__name__)
        self.payload=Payload(API())
        self.Header=Header()
        