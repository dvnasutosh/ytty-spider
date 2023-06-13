from betterdataclass.StrictDictionary import StrictDictionary
from .ChannelMeta import browseEndpoint

class ShelfDetails(StrictDictionary):
    title           :   str
    subtitle        :   str
    browseEndpoint  :   browseEndpoint
    data            :   list