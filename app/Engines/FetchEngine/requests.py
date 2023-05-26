from urllib.parse import urlencode
import requests
import json
from enum import Enum

from betterdataclass.StrictDictionary import StrictDictionary
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
    
class Header(dict):
    def __init__(self,Auth:Authentication=Authentication()) -> None:
        super().__setitem__('cookie',json.dumps(Auth.cookie))
   
class PF(Enum):
    EMBED={
        "clientName": "WEB_EMBEDDED_PLAYER",
        "clientVersion": "1.20230131.01.00",
    }
    WEB={
        
        "clientName": "WEB",
        "clientVersion": "2.20230213.01.00"
    }
    ANDROID={
            "clientName": "ANDROID",
            "clientVersion": "18.10.36",
    }
    TV={
        "clientName": "TVHTML5_SIMPLY_EMBEDDED_PLAYER",
        "clientVersion": "2.0"
    }

class CONTEXT(StrictDictionary):
    gl:str='IN'
    hl:str='en'

class Payload(dict):
    def __init__(self,client:CONTEXT,Uparam:dict=dict(),PF=PF.WEB) -> None:
        
        self.__setitem__('context',{'client':client()})
    
        self.setClient(**PF.value)
       
    # Setting UParam If Exists
        self.setUParam(**Uparam)

    def setUParam(self,**UParam)->None:
        for i,j in UParam.items():
            self[i]=j

    def setClient(self,**client):
        for i,j in client.items():
            self['context']['client'][i]=j
    
class endpoint_base:
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        return self.__name__
    
    def __repr__(self)->str:
        return json.dumps(self.__dict__)

class yt_requests:
    def __init__(self,auth:Authentication=Authentication(),client:CONTEXT=CONTEXT()):
    
        
        # Setting Header if context given
        self.HEADER=Header(auth)
        
        self.raw:requests.Response
        
        #Checking if the client data provided is CONTEXT or not
        if not isinstance(client, CONTEXT):
            raise TypeError(f"client is not of type CONTEXT.")

        # Setting client if context given
        self.PAYLOAD.setClient(**(client()))
        

    def __init_subclass__(cls) -> None:

        if not issubclass(cls,endpoint_base):
            raise TypeError('doesn\'t inherit Endpoint_Base')
        cls.URL = URL(cls.__name__) 
        cls.PAYLOAD = Payload(client=CONTEXT())

    def UpdateContext(self, client:CONTEXT):
        if not isinstance(client, CONTEXT):
            raise TypeError(f"client is not of type CONTEXT.")
        
        # Setting client if context given
        self.PAYLOAD.setClient(**(client()))
    
    def UpdatePF(self,PlatForm:PF):
        if not isinstance(PlatForm, PF):
            raise TypeError("Atribute not of type PF")
        
        self.PAYLOAD.setClient(**(PlatForm.value))

    def Fetch(self)-> requests.Response:
        return requests.post(url=self.URL,data=json.dumps(self.PAYLOAD),headers=self.HEADER)