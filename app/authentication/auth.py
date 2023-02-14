import requests
class Auth:
    
    def __init__(self) -> None:
        
        self.__ytinit=requests.get('https://www.youtube.com')
        self.cookie=dict(self.__ytinit.cookies)
        
    staticmethod
    def get_cookies():
        return dict(requests.get('https://www.youtube.com').cookies)