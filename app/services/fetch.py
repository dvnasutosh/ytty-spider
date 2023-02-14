from type.fetchType import fetchType

from app.authentication.auth import Auth
class fetchEngine(Auth):
    def __init__(self,Rtype:fetchType) -> None:
        self.context=Rtype
        setattr()
