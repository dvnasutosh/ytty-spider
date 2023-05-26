# from app.Engines.RestEngine.Validation import Options
# from app.services.videoManager import videoManager as vm
from ast import arg
from math import e
from flask import Blueprint, request
from app.Engines.RestEngine.Validation import Validate
from app.services.videoManager import videoManager
from betterdataclass.helper.to_dict import to_raw_dict

video_routes=Blueprint("video_routes",__name__)

@video_routes.route('/video/details',methods=['POST','GET'])
def get_video_details():
    try:
        args = Validate.video.Details(**request.args)
        
    except Exception as e:
        return {"error":e},400
    
    if not request.args:
        return {"error":"videoId required"},400
      
    if request.method=='POST':
        try:
            Opt=Validate.Common.Options(request.JSON)
        except TypeError as e:
            return {"Error":str(e)},400
        video=videoManager(videoId=request.args['videoId'],context=Opt())
    elif request.method=='GET':
        video=videoManager(videoId=request.args['videoId'])

    return {
        'details':video.Details()(True)
    }
    