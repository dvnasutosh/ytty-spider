from betterdataclasses.betterdataclass.StrictDictionary import StrictDictionary
from ..common import browseEndpoint

class ShelfDetails(StrictDictionary):
    title           :   str
    subtitle        :   str
    browseEndpoint  :   browseEndpoint
    data            :   list