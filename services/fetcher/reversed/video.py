from model.WebDriver import webDriver
import json
import requests
import time
from services.helper.deserialise import deserialise_videoData
def get_videoData(
    videoId:str,
    # cookie:str
    ):
    videoData=dict()
    url = "https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"
    sel=webDriver(isHeadless=True)
    sel.goto('https://www.youtube.com')
    cookie=sel.getCookies(iRaw=True)
    payload = json.dumps({
    "videoId": videoId,
    "context": {
        "client": {
        "hl": "en",
        "gl": "IN",
        "remoteHost": "2401:4900:1cb8:b32f:ddc7:f815:9cce:eb84",
        "deviceMake": "",
        "deviceModel": "",
        "visitorData": "CgtLZ2cxTmFGZXhMOCjlnP-eBg%3D%3D",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36,gzip(gfe)",
        "clientName": "WEB_EMBEDDED_PLAYER",
        "clientVersion": "1.20230131.01.00",
        "osName": "Windows",
        "osVersion": "10.0",
        "originalUrl": "https://www.youtube.com/embed?controls=0&enablejsapi=1&iv_load_policy=3&modestbranding=1&mute=1&rel=0&showinfo=0&origin=https%3A%2F%2Fwww.youtube.com&widgetid=1",
        "platform": "DESKTOP",
        "clientFormFactor": "UNKNOWN_FORM_FACTOR",
        "configInfo": {
            "appInstallData": "COWc_54GEMzfrgUQ1-SuBRDa6a4FELiLrgUQ5_euBRCwpP4SELL1rgUQioCvBRDrov4SEILdrgUQ5KD-EhCH3a4FEKP5rgU%3D"
        },
        "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
        "timeZone": "Asia/Calcutta",
        "browserName": "Chrome",
        "browserVersion": "109.0.0.0",
        "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "deviceExperimentId": "ChxOekU1TmpZNU5qWTNOVGc0TURJd01EWTJNUT09EOWc_54GGP-a_54G",
        "screenWidthPoints": 424,
        "screenHeightPoints": 238,
        "screenPixelDensity": 1,
        "screenDensityFloat": 0.8999999761581421,
        "utcOffsetMinutes": 330,
        "connectionType": "CONN_CELLULAR_4G",
        "playerType": "UNIPLAYER",
        "tvAppInfo": {
            "livingRoomAppMode": "LIVING_ROOM_APP_MODE_UNSPECIFIED"
        },
        "clientScreen": "ADUNIT"
        },
        "user": {
        "lockedSafetyMode": False
        },
        "request": {
        "useSsl": True,
        "consistencyTokenJars": [
            {
            "encryptedTokenJarContents": "AEhaiyvPi0oJGKV-tCZpWtQZxzWooba8S0Le72a2d8QN3knZB38K2yF_BmasrVQWIsVr4SuQy-9-IAf8NwEWjry0nCw4fsZlJsQTsxkMMR5h3K5_PgTwlhuyvV65a7xtvSn25ZvVle-uC0AG6pT8P2o"
            }
        ],
        "internalExperimentFlags": []
        },
        "clientScreenNonce": "UNDEFINED_CSN",
        "adSignalsInfo": {
        "params": [
            {
            "key": "dt",
            "value": "1675611738207"
            },
            {
            "key": "flash",
            "value": "0"
            },
            {
            "key": "frm",
            "value": "1"
            },
            {
            "key": "u_tz",
            "value": "330"
            },
            {
            "key": "u_his",
            "value": "3"
            },
            {
            "key": "u_h",
            "value": "1080"
            },
            {
            "key": "u_w",
            "value": "1920"
            },
            {
            "key": "u_ah",
            "value": "1032"
            },
            {
            "key": "u_aw",
            "value": "1920"
            },
            {
            "key": "u_cd",
            "value": "24"
            },
            {
            "key": "bc",
            "value": "31"
            },
            {
            "key": "bih",
            "value": "1013"
            },
            {
            "key": "biw",
            "value": "995"
            },
            {
            "key": "brdim",
            "value": "627,219,627,219,1920,0,926,1032,424,238"
            },
            {
            "key": "vis",
            "value": "1"
            },
            {
            "key": "wgl",
            "value": "true"
            },
            {
            "key": "ca_type",
            "value": "image"
            }
        ]
        },
        "thirdParty": {
        "embedUrl": "https://www.youtube.com/"
        }
    },
    "playbackContext": {
        "contentPlaybackContext": {
        "html5Preference": "HTML5_PREF_WANTS",
        "lactMilliseconds": "84",
        "referer": "https://www.youtube.com/embed/?controls=0&enablejsapi=1&iv_load_policy=3&modestbranding=1&mute=1&rel=0&showinfo=0&origin=https%3A%2F%2Fwww.youtube.com&widgetid=1",
        "signatureTimestamp": 19389,
        "autoCaptionsDefaultOn": False,
        "mdxContext": {},
        "playerWidthPixels": 424,
        "playerHeightPixels": 239,
        "ancestorOrigins": [
            "https://www.youtube.com"
        ]
        }
    },
    "cpn": "8CmUGpJXjQIl3xBN",
    "params": "CkoIERAIQhdZODdmWTdDWEVadk80dDRQeHBHbi1BNIoDJyADKAIwBjgIShMI8NTpl9z-_AIVG6fYBR3GyAnvUgQIAlgBaAFwPJgDAWAB",
    "captionParams": {}
    })
    headers = {
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="99.0.0.0", "Google Chrome";v="109.0.5414.120", "Chromium";v="109.0.5414.120"',
    'sec-ch-ua-wow64': '?0',
    'sec-ch-ua-model': '',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-platform': '"Windows"',
    'X-Youtube-Bootstrap-Logged-In': 'false',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'sec-ch-ua-full-version': '"109.0.5414.120"',
    'X-Youtube-Client-Name': '56',
    'X-Youtube-Client-Version': '1.20230131.01.00',
    'X-Goog-Visitor-Id': 'CgtLZ2cxTmFGZXhMOCjlnP-eBg%3D%3D',
    'Accept': '*/*',
    'host': 'www.youtube.com',
    'cookie': json.dumps(cookie)
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    #converting the recieved data into Dictionary
    raw_data=json.loads(response.text)
    return deserialise_videoData(raw_data)
get_videoData('iozXJZGfCUU')


