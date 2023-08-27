# from app.Engines.RestEngine.Validation import Options
# from app.services.videoManager import videoManager as vm

from flask import Blueprint, request
from app.Engines.RestEngine.Validation import Validate
from app.dataclass.videoDC.Comments import Comments
from app.services.videoManager import videoManager
from betterdataclasses.betterdataclass.helper.to_dict import to_raw_dict

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

    return {

        'comments':video.comments(**args())(True)}

@video_routes.route('/video/comments/reply',methods=['POST','GET'])
def get_video_comments_reply():
    """
        - Not a necessary route. everything comments related can be attained from /video/comments
    """
    try:
        args = Validate.video.Comments(**request.args)
        if not (args.continuation):
            raise AttributeError("videoId not allowed while fetching reply")
    except Exception as e:
        return {"error":e},400
    
    if request.args.keys().__len__()!=1 or 'continuation' not in request.args.keys():
        return {"error":"Invalid query:Only continuation allowed as param"},400
    if request.method=='POST':
        try:
            Opt=Validate.Common.Options(request.JSON)
        except TypeError as e:
            return {"Error":str(e)},400

        video=videoManager(context=Opt())
    elif request.method=='GET':
        video=videoManager()

    return {
        'reply':video.comments(continuation=args['continuation'],continued=True)(True)
        }


@video_routes.route('/video/downloads',methods=['POST','GET'])
def get_video_downloads():
    
    try:
        args = Validate.video.Details(**request.args)
    
    except Exception as e:
        return {"error":e},400
    
    if request.method=='POST':
        try:
            Opt=Validate.Common.Options(request.JSON)
        except TypeError as e:
            return {"Error":str(e)},400

        video=videoManager(videoId=request.args['videoId'],context=Opt())
    
    elif request.method=='GET':
        video=videoManager(videoId=request.args['videoId'])
    
    return {
        'download':video.Download()(True),
    }


