from json import loads,dumps


from app.authentication.auth import Authentication
from app.fetchHandler.endpoint import next, player
from app.fetchHandler.requests import CONTEXT

from app.dataHandler.deserialise import Deserialise


class videoManager:
    def __init__(self, videoId: str = None, auth: Authentication = Authentication(), context: CONTEXT = CONTEXT()):
        self.videoId = videoId
        self.next = next(auth=auth, client=context)
        self.player = player(auth=auth, client=context)
        if videoId:
            self.details = self.fetchDetails(videoId)

    def updateContext(self, context: CONTEXT):
        self.next.UpdateContext(context)
        self.player.UpdateContext(context)

    def fetchDetails(self, videoId: str):
        return Deserialise.videoData(loads(self.player(videoId).text))
        # return loads(self.player(videoId).text)


x = videoManager()
# print(  
#     dumps(x.fetchDetails('a_7zDL3_YPM')['videoDetails'], indent=4)
#     )
print(x.fetchDetails('a_7zDL3_YPM'))