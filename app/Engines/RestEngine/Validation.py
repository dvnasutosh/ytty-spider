from betterdataclass.StrictDictionary import StrictDictionary,Dictionary

    
class TabRoute(StrictDictionary):
    params:str
    channelId:str    

class Validate:
    # Validation Purpose
    class video:
        class Details(StrictDictionary):
            videoId:str
    class Common:
        class Options(StrictDictionary):
            hl:str
            gl:str
            
            