# from app.Engines.RestEngine.Validation import Options
# from app.services.videoManager import videoManager as vm
from ast import arg
from math import e
from flask import Blueprint, request
from app.Engines.RestEngine.Validation import Validate
from app.dataclass.videoDC.Comments import Comments
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
        video=videoManager(videoId=args.videoId,context=Opt())
    
    elif request.method=='GET':
        video=videoManager(videoId=args.videoId)

    return {
        'details':video.Details()(True)
    }

@video_routes.route('/video/interactions',methods=['POST','GET'])
def get_video_interactions():
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
        video=videoManager(videoId=args.videoId,context=Opt())
    elif request.method=='GET':
        video=videoManager(videoId=args.videoId)

    return {
        'interactions':video.interactionData()(True)
        }


@video_routes.route('/video/comments',methods=['POST','GET'])
def get_video_comments():
    
    # Route Validation
    try:
        args = Validate.video.Comments(**request.args)
    except Exception as e:
        return {"error":e},400
    # print(args(True))
    if not any(args().keys()):
        return {"error":"Invalid query:either 1 or 2 args allowed only"},400

    if request.method=='POST':
        try:
            Opt= Validate.Common.Options(request.JSON)
        except TypeError as e:
            return {"Error":str(e)},400
        video=videoManager(context=Opt())
    elif request.method=='GET':
        video=videoManager()
    # print()
    # print()
    # print()
    # print(video.comments(**args())())
    # print()
    # print()
    # print()
    return {
        # 'comments':video.comments(**args())}
        'comments':video.comments(**args())(True)}