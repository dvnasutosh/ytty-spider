from app.type.Base import DynamicMembers
from typing import List, Dict
from pydantic import BaseModel

class Video(DynamicMembers):
    videoId: str
    title: str
    author: str
    lengthSeconds: str
    keywords: List[str]
    channelId: str
    shortDescription: str
    video: List[Dict]
    isOnwerViewing: bool
    isCrawlable: bool
    allowRating: bool
    isPrivate: bool
    isLiveContent: bool
    data: dict
video = Video()
video['videoId'] = '123456'
video['title'] = 'My Video Title'
video['author'] = 'Author Name'
video['lengthSeconds'] = '600'
video['keywords'] = ['video', 'content', 'entertainment']
video['channelId'] = 'ABC123'
video['shortDescription'] = 'A short description of the video'
video['video'] = [{'url': 'http://video.com/video1', 'format': 'mp4'}, {'url': 'http://video.com/video2', 'format': 'webm'}]
video['isOnwerViewing'] = True
video['isCrawlable'] = False
video['allowRating'] = True
video['isPrivate'] = False
video['isLiveContent'] = False
