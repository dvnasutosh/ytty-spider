from app.Engines.RestEngine.Validation import TabRoute
from app.dataclass.channelDC.ChannelMeta import browseEndpoint
from flask import Flask,request,Response,Blueprint

from app.services.channelManager import channelManager


channel_routes=Blueprint("channel_routes",__name__)

@channel_routes.get('/test')
def test():
    return "Valid"

@channel_routes.get('/<t>/continue')
def test2(t):
    return t

@channel_routes.get('/channel/<tab>')
def channel_tabs(tab):
    #   Validating query parameters
    try:
        query=TabRoute(**request.args)
        if not query.channelId:
            raise AttributeError("ChannelId necessary")
        
    except Exception as e:
        return {"error":e},400
    
    cM=channelManager(channelId=query.channelId)
    
    
    try:
        data=getattr(cM,str.capitalize(tab))
    except AttributeError:
        return {"error":"Invalid tab"},400
    except Exception as e:
        return {"error":e}
    
    return {"data":data().__raw__()}


@channel_routes.post('/channel')
def channel_tabs_post():
    
    #Checking For body data
    try:
        browse= browseEndpoint(**request.json)
    except Exception:
        return {
            "message":"Invalid query",
            "error":Exception,
            "json": request.json      
        },400
    
    cM=channelManager().Tab(browse=browse)
    return {"data":cM.__raw__()}





















    # if str.lower(tab)=="home":
    # elif str.lower(tab)=="videos":
    #     pass
    # elif str.lower(tab)=="shorts":
    #     pass
    # elif str.lower(tab)=="playlists":
    #     pass
    # elif str.lower(tab)=="community":
    #     pass
    # elif str.lower(tab)=="channels":
    #     pass
    # elif str.lower(tab)=="search":
    #     pass
    