
import json

from app.authentication.auth import Authentication
from app.Engines.FetchEngine.requests import CONTEXT, endpoint_base, yt_requests


class next(yt_requests,endpoint_base):
    
    def __call__(self,videoId:str='',continuation:str=''):
        if videoId=='' and continuation=='':
            raise ValueError('Either video_id or continuation must be provided.')

        self.PAYLOAD.setUParam(videoId=videoId,continuation=continuation)

        self.raw=self.Fetch()
        return self.raw
                

class player(yt_requests,endpoint_base):
    
    def __call__(self,videoId:str):

        self.PAYLOAD.setUParam(videoId=videoId)
        

        self.raw=self.Fetch()
        return self.raw

class search(yt_requests,endpoint_base):
    
    def __call__(self,query:str):
        self.PAYLOAD.setUParam(query=query)
        
        self.raw=self.Fetch()
        return self.raw

class browse(yt_requests,endpoint_base):
    
    def __call__(self,browseId:str=bool(),params:str=bool(),continuation=bool(),canonicalBaseUrl=bool()):
        
        
        if continuation != False:
            self.PAYLOAD.setUParam(continuation=continuation)
        if browseId != False:
            self.PAYLOAD.setUParam(browseId=browseId)
        if params != False:
            self.PAYLOAD.setUParam(params=params)
        if not (continuation or (params and browseId) or browseId):
            self.PAYLOAD.setUParam(browseId=browseId,params=params,continuation=continuation)
        if canonicalBaseUrl != False:
            self.PAYLOAD.setUParam(canonicalBaseUrl=canonicalBaseUrl)
            
        self.raw=self.Fetch()
        return self.raw