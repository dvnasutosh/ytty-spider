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

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5002,debug=False,threaded=True)
# TODO: Channel Home - > both continuation and basic content
