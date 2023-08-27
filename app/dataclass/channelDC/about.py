from app.dataclass.common import dateInt
from betterdataclasses.betterdataclass.StrictDictionary import StrictDictionary

class aboutChannel(StrictDictionary):
    description:str
    viewCount:int
    joinedDate:int
    country:str
    
