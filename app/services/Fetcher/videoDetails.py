import json
import requests

from app.services.DataManager.deserialise import deserialise_videoData,deserialise_interactionData

from app.common.urls import url
from app.common.payload import generalPayloadWEB
  
    

def get_videoData(
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

def get_videoInteractions(
    videoId:str
)->str:
    response =requests.request('POST',url['next'],data=json.dumps(generalPayloadWEB(videoId)))

    
    return deserialise_interactionData(json.loads(response.text))

    
data=get_videoInteractions("BddP6PYo2gs")

print(data)
