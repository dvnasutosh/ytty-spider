from flask import Flask,request,Response,Blueprint
from app.services.channelManager import channelManager

channel_routes=Blueprint("channel_routes",__name__)

@channel_routes.get('/test')
def test():
    return "Valid"
@channel_routes.get('/channel/<tab>')
def channel_tabs(tab):
    if not request.args.keys().__len__() in (1,2):
        return {"error":"Invalid query: only 1, or 2 params are allowed"},400
    
    if not "channelId" in request.args.keys():
        return {"error":"Invalid query: channelId essential as query"},400
    
    cM=channelManager(channelId=request.args.get('channelId'))
    
    try:
        data=getattr(cM,str.capitalize(tab))
    except AttributeError:
        return {"error":"Invalid tab"},400
    except Exception as e:
        return {"error":e}
    
    return {"data":data().__raw__()}

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
    