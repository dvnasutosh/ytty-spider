from urllib.parse import urlencode
import requests
import json
from enum import Enum

from app.type.Base import StrictDictionary
from app.authentication.auth import Authentication

class ResourceName(Enum):
    API:str=r'https://www.youtube.com/'
    # SHint:str=r'https://suggestqueries-clients6.youtube.com/'

class Route:
    route_path=r'youtubei/v1/'
    # SHint=r'complete/'    TODO: Adding a separate pathway for search hinting
    def __init__(self,ROUTE) -> None:
        self.__path=self.route_path+str(ROUTE)
    def __repr__(self) -> str:
        return self.__path

class queryString:
    basic={'key':'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'}
    # searchQuery=dict({
    #     'client':'youtube',
    #     'q':None})
    
class URL:
    def __init__(self,Endpoint:str) -> None:
         self.__data= ResourceName.API.value+str(Route(Endpoint))+"?"+urlencode(queryString.basic)
         
    def __repr__(self) -> str:
        return self.__data
    
class Header:
    def __init__(self,Auth=dict()) -> None:
        if not Auth:
            self.data=Auth
            
    def __repr__(self) -> str:
        return json.dumps(self.data)

class PF(Enum):
    EMBED={
    
        "clientName": "WEB_EMBEDDED_PLAYER",
        "clientVersion": "1.20230131.01.00",
        }
    WEB={
        
        "clientName": "WEB",
        "clientVersion": "2.20230213.01.00"
    }

class CONTEXT(StrictDictionary):
    gl:str='IN'
    hl:str='en'
    


class Payload:
    def __init__(self,client:CONTEXT,Uparam:dict=dict(),PF=PF.WEB) -> None:
        
        self._data={'context':{'client':client()}}
    
        self.setClient(**PF.value)
       
    # Setting UParam If Exists
        self.setUParam(**Uparam)

    def setUParam(self,**UParam)->None:
        for i,j in UParam.items():
            self._data[i]=j

    def setClient(self,**client):
        for i,j in client.items():
            self._data['context']['client'][i]=j
    
    def __repr__(self) -> str:
        return json.dumps(self._data)
    def __call__(self) -> dict:
        self._data
    
        
    def __setitem__(self,__name,__value):
        self._data[__name]=__value
    
    def __getitem__(self,__name):
        return self.__data[__name]

class yt_requests:
    def __init__(self,auth:Authentication,client:CONTEXT):
    
        self.URL:URL
        self.PAYLOAD:Payload
        self.HEADER:Header
        
        # Setting client if context given
        self.PAYLOAD.setClient(**(client()))
        
        # Setting Header if context given
        self.HEADER=Header(auth)
    
    
    
    
    def __init_subclass__(cls) -> None:
        print('Entered initsub')
        if not issubclass(cls,endpoint_base):
            raise TypeError('doesn\'t inherit Endpoint_Base')
        cls.URL = URL(cls.__name__) 
        cls.PAYLOAD = Payload(client=CONTEXT())
        
    def Fetch(self)-> requests.Request:
        return requests.request(method='POST',url=self.URL,data=self.PAYLOAD,headers=self.HEADER)

    # def setUparam(self,**param):
    #     self.PAYLOAD.setUParam(**param)

class endpoint_base:
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        return self.__name__
    
    def __repr__(self)->str:
        return json.dumps(self.__dict__)

