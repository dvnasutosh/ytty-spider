# from app.Engines.RestEngine.Validation import Options
# from app.dataclass.channelDC.ChannelMeta import browseEndpoint

# import json

from flask import Flask


# from app.services.channelManager import channelManager as cm
# from app.services.videoManager import videoManager as vm
from app.Engines.RestEngine.Routes.channel import channel_routes
from app.Engines.RestEngine.Routes.video import video_routes
app = Flask(__name__)

app.register_blueprint(channel_routes)
app.register_blueprint(video_routes)

@app.route('/',methods=['POST','GET'])
def home():
    return "Hello"
    

# # @app.route('/channel',method=['POST','GET'])

# @app.route('/channel/details',methods=['POST','GET'])
# def get_channel_details():
#     if 1<=request.args.keys().__len__()<3 and "channelId" in request.args.keys():
#         return {"error":"Invalid query: channelId neccesary"}
    
#     if request.method=='POST':
#         try:
#             Opt=Options(request.JSON)
#         except TypeError as e:
#             return {"Error":str(e)},400

#         chObj=cm(context=Opt())
#         chDetails=chObj.Details(channelId=request.args['channelId'])
#     elif request.method=='GET':
#         chObj=cm()
#         chDetails=chObj.Details(channelId=request.args['channelId'])
#     else:
#         return {"Error":"GET OR POST ALLOWED ONLY."},400
    
#     return {"channel_details":chDetails.__raw__()}

# @app.route('/channel/home',methods=['POST','GET'])
# def get_channel_home():
#     if request.args.keys().__len__()!=1 and "params" in request.args.keys():
#         return {"error":"Invalid query: params essential as query"}
    
#     if request.method=='POST':
#         try:
#             Opt=Options(request.JSON)
#         except TypeError as e:
#             return {"Error":str(e)},400
    
#         chObj=cm(context=Opt())
#         chDetails=chObj.Details(channelId=request.args['channelId'])
#     elif request.method=='GET':
#         chObj=cm()
#         chDetails=chObj.Details(channelId=request.args['channelId'])
#     else:
#         return {"Error":"GET OR POST ALLOWED ONLY."},400
    
#     return {"channel_details":chDetails.__raw__()}


# def beauty(data:dict):
#     return json.dumps({"json":data},indent=4)


# def Test():
    
#     browse= browseEndpoint(browseId='UCsBjURrPoezykLs9EqgamOA',params='')

#     content=cm().Tab(browse=browse)
#     contentComplete = {}
#     beauty(content)
#     # for i in content.tabs:
#     #     contentComplete[i.title]=cm().Tab(i.browseEndpoint).__raw__()
#     #     print(json.dumps(contentComplete,indent=4))

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5002,debug=True)

# TODO: Channel Home - > both continuation and basic content