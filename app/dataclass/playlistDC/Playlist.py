from betterdataclass.StrictDictionary import StrictDictionary
from app.dataclass.common import img, strbool
from app.dataclass.ChannelDataClasses.ChannelMeta import browseEndpoint

class Playlist(StrictDictionary):
    title:str
    playlistId:str
    description:str
    privacy:str
    canDelete:strbool
    isEditable:strbool
    canShare:strbool
    videosCount:int
    ownerEndpoint:browseEndpoint
    playlistHeaderBanner:img
    playlistViews:int

class PlaylistMini(StrictDictionary):
    ownerBadges:bool
    playlistId:bool
    thumbnail:img
    title:str
    videosCount:int