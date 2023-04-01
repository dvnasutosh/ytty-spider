
from app.fetchHandler.requests import endpoint_base,yt_requests,CONTEXT
from app.authentication.auth import Authentication

import json

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
    
    def __call__(self,browseId:str=str(),param:str=str(),continuation=str()):
        if continuation:
            self.PAYLOAD.setUParam(continuation=continuation)
        elif not param and browseId:
            self.PAYLOAD.setUParam(browseId=browseId)
        else:
            self.PAYLOAD.setUParam(browseId=browseId,param=param,continuation=continuation)
            
        self.raw=self.Fetch()
        return self.raw