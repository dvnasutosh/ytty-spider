import requests
class Authentication:
    
    def __init__(self,data=None) -> None:
        
        self.__ytinit=requests.get('https://www.youtube.com')
        self.cookie=dict(self.__ytinit.cookies)
        
    staticmethod
    def get_cookies():
        return dict(requests.get('https://www.youtube.com').cookies)