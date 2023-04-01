from app.dataclass.Base import StrictDictionary

class Interactions(StrictDictionary):
    """stores all interactions relative to a youtube video

    Args:
        StrictDictionary (dict): _description_
    """
    likes:int
    comments_continuation:str

