from enum import Enum




def constructPayload(key: str, value: str, type: contextType):
    type[key] = value
    return type




webContext: dict = {"context": {
    "client": {
        "clientName": "WEB_EMBEDDED_PLAYER",
        "clientVersion": "1.20230131.01.00",
    }
}}

generalPayloadEMBED: dict = lambda videoId: {
    """_summary_: payload for embedded video endpoint

"""
    "videoId": videoId,
    "context": {
        "client": {
            "clientName": "WEB_EMBEDDED_PLAYER",
            "clientVersion": "1.20230131.01.00",
        }
    }
}
generalPayloadWEB: dict = lambda videoId: {
    "videoId": videoId,
    "context": 
}
commentPayload: dict = lambda continuation: {
    "continuation": continuation,
    "context": {
        "client": {
            "clientName": "WEB",
            "clientVersion": "2.20230213.01.00"
        }
    }
}
