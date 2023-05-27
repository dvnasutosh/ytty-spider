from betterdataclass.StrictDictionary import StrictDictionary
from app.dataclass.ChannelDataClasses.ChannelMeta import browseEndpoint

class ShelfDetails(StrictDictionary):
    title           :   str
    subtitle        :   str
    browseEndpoint  :   browseEndpoint
    data            :   list