from typing import Union
import requests
class Authentication:
    
    def __init__(self) -> None:
        self.__ytinit=requests.get(url='https://www.youtube.com')
        self.cookie=dict(self.__ytinit.cookies)
    
    def set_cookies(self,cookie:Union[dict,str]):
        self.cookie=cookie
    @staticmethod
    def get_cookies():
        return dict(requests.get('https://www.youtube.com').cookies)
    
    