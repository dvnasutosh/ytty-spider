
from app.fetchHandler.Requests import endpoint_base,yt_requests,CONTEXT
from app.authentication.auth import Authentication
class next(yt_requests,endpoint_base):
    
    def __init__(self, 
                 Auth:Authentication,
                 CONTEXT:CONTEXT=CONTEXT()) -> None:
        super().__init__(Auth,client=CONTEXT)
        
        self.raw:dict
        
    def __call__(self,videoId:str='',continuation:str='')->None:
        if videoId=='' and continuation=='':
            raise ValueError('Either video_id or continuation must be provided.')
        self.PAYLOAD.setUParam(videoId=videoId,continuation=continuation)
        self.raw=self.Fetch()
        return self.raw
                


"""
next(Auth(),CONTEXT())
Youtube.next(videoId,Continuation).
        
        """
        
x=Authentication()   
print(next(Auth=x)('UH8f9NJQXEI'))
