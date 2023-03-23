from flask import Flask,request,Response
from app.services.videoManager import videoManager as vm
from app.RESTHandler.Validation import Options
app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def home():
    return "Hello"
    
@app.route('/video',methods=['POST','GET'])
def get_video():
    
    #Handling Validation Error
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
        'details':video.Details().__raw__(),
        'download':video.Download().__raw__(),
        'interactions':video.interactionData().__raw__()
    }


@app.route('/video/details',methods=['POST','GET'])
def get_video_details():
    return 'Temp video Details returned'

@app.route('/video/interactions',methods=['POST','GET'])
def get_video_interactions():
    return 'Temp interaction Details returned'





@app.route('/video/comments',methods=['POST','GET'])
def get_video_comments():
    return 'Temp comments Details returned'

@app.route('/video/Downloads',methods=['POST','GET'])
def get_video_downloads():

    return 'Temp comments Details returned'


import json
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002,debug=True)

