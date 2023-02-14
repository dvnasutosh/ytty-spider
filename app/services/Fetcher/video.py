import json
import requests

from app.services.DataManager.deserialise import deserialise_videoData






def get_videoData2(
    videoId:str,
    ):
    url = "https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"
    
    payload = json.dumps({
    "videoId": videoId,
    "context": {
        "client": {
        "clientName": "WEB_EMBEDDED_PLAYER",
        "clientVersion": "1.20230131.01.00",
        },
    }
    })
    
    response = requests.request("POST", url, data=payload)
    
    #converting the recieved data into Dictionary
    raw_data=json.loads(response.text)
    return deserialise_videoData(raw_data)

def getVdoLikes(
    videoId:str
)
y=get_videoData2("BddP6PYo2gs")
print(json.dumps(y,indent=2))


