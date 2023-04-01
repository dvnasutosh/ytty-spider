from flask import Flask,request,Response
from app.services.videoManager import videoManager as vm
from app.services.channelManager import channelManager as cm
from app.RESTHandler.Validation import Options
import json

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def home():
    return "Hello"
    
@app.route('/video',methods=['POST','GET'])
def get_video():
    
    #Handling Validation Error
    if request.args.keys().__len__()!=1 and "videoId" in request.args.keys():
        return {"error":"Invalid query:only videoId allowed as param"},400
    
    if request.method=='POST':
        try:
            Opt=Options(request.JSON)
        except TypeError as e:
            return {Error:str(e)},400

        video=vm(videoId=request.args['videoId'],context=Opt())
    elif request.method=='GET':
        video=vm(videoId=request.args['videoId'])

    return {
        'details':video.Details().__raw__(),
        'download':video.Download().__raw__(),
        'interactions':video.interactionData().__raw__()
    }


@app.route('/video/details',methods=['POST','GET'])
def get_video_details():
    if request.args.keys().__len__()!=1 and "videoId" in request.args.keys():
        return {"error":"Invalid query:only videoId allowed as param"},400
    
    if request.method=='POST':
        try:
            Opt=Options(request.JSON)
        except TypeError as e:
            return {Error:str(e)},400

        video=vm(videoId=request.args['videoId'],context=Opt())
    elif request.method=='GET':
        video=vm(videoId=request.args['videoId'])

    return {
        'details':video.Details().__raw__()
    }

@app.route('/video/interactions',methods=['POST','GET'])
def get_video_interactions():
    if request.args.keys().__len__()!=1 and "videoId" in request.args.keys():
            return {"error":"Invalid query:only videoId allowed as param"},400
        
    if request.method=='POST':
        try:
            Opt=Options(request.JSON)
        except TypeError as e:
            return {Error:str(e)},400

        video=vm(videoId=request.args['videoId'],context=Opt())
    elif request.method=='GET':
        video=vm(videoId=request.args['videoId'])

    return {
        'interactions':video.interactionData().__raw__()
        }


@app.route('/video/comments',methods=['POST','GET'])
def get_video_comments():
    videoId:str=''
    continuation:str=''

    if not (0<request.args.keys().__len__()<=2):
            return {"error":"Invalid query:either 1 or 2 args allowed only"},400
    
    if "continuation" not in request.args.keys():
        if "videoId" not in request.args.keys():
            return {"error":"Invalid query:neither videoId nor continuation provided"}
        else:
            videoId=request.args['videoId']
    else:
        continuation=request.args['continuation']
            
        


    if request.method=='POST':
        try:
            Opt=Options(request.JSON)
        except TypeError as e:
            return {Error:str(e)},400
        video=vm(context=Opt())
    elif request.method=='GET':
        video=vm()
    return {
        'comments':video.comments(videoId=videoId,continuation=continuation).__raw__()}

@app.route('/video/comments/reply',methods=['POST','GET'])
def get_video_comments_reply():
    if request.args.keys().__len__()!=1 or 'continuation' not in request.args.keys():
        return {"error":"Invalid query:Only continuation allowed as param"},400
    if request.method=='POST':
        try:
            Opt=Options(request.JSON)
        except TypeError as e:
            return {Error:str(e)},400

        video=vm(context=Opt())
    elif request.method=='GET':
        video=vm()

    return {
        'continued':video.comments(continuation=request.args['continuation'],continued=True).__raw__()
        }

@app.route('/video/downloads',methods=['POST','GET'])
def get_video_downloads():
    if request.args.keys().__len__()!=1 and "videoId" in request.args.keys():
        return {"error":"Invalid query:only videoId allowed as param"}

    if request.method=='POST':
        try:
            Opt=Options(request.JSON)
        except TypeError as e:
            return {Error:str(e)},400

        video=vm(videoId=request.args['videoId'],context=Opt())
    elif request.method=='GET':
        video=vm(videoId=request.args['videoId'])

    return {
        'download':video.Download().__raw__(),
    }

# @app.route('/channel',method=['POST','GET'])

@app.route('/channel/details',methods=['POST','GET'])
def get_channel_details():
    if 1<=request.args.keys().__len__()<3 and "channelId" in request.args.keys():
        return {"error":"Invalid query: channelId neccesary"}
    
    if request.method=='POST':
        try:
            Opt=Options(request.JSON)
        except TypeError as e:
            return {Error:str(e)},400

        chObj=cm(context=Opt())
        chDetails=chObj.Details(channelId=request.args['channelId'])
    elif request.method=='GET':
        chObj=cm()
        chDetails=chObj.Details(channelId=request.args['channelId'])
    else:
        return {Error:"GET OR POST ALLOWED ONLY."},400
    
    return {"channel_details":chDetails.__raw__()}

@app.route('/channel/home',methods=['POST','GET'])
def get_channel_home():
    if request.args.keys().__len__()!=1 and "params" in request.args.keys():
        return {"error":"Invalid query: params essential as query"}
    
    if request.method=='POST':
        try:
            Opt=Options(request.JSON)
        except TypeError as e:
            return {Error:str(e)},400
    
        chObj=cm(context=Opt())
        chDetails=chObj.Details(channelId=request.args['channelId'])
    elif request.method=='GET':
        chObj=cm()
        chDetails=chObj.Details(channelId=request.args['channelId'])
    else:
        return {Error:"GET OR POST ALLOWED ONLY."},400
    
    return {"channel_details":chDetails.__raw__()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002,debug=True)

# TODO: Channel Home - > both continuation and basic content
#  