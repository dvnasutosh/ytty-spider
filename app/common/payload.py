

generalPayloadEMBED: dict = lambda videoId: {
"""_summary_: payload for embedded video endpoint

"""
    "videoId": videoId,
    "context": {
        "client": {
            "clientName": "WEB_EMBEDDED_PLAYER",
            "clientVersion": "1.20230131.01.00",
        },
    }
}
generalPayloadWEB: dict = lambda videoId: {
    "videoId": videoId,
    "context": {
        "client": {
            "clientName": "WEB",
            "clientVersion": "2.20230213.01.00"
        }
    }
}
