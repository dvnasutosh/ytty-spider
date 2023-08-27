

from betterdataclasses.betterdataclass.StrictDictionary import StrictDictionary
from app.dataclass.common import img, url


class Product(StrictDictionary):
    title:str
    thumbnail:img
    url:url
    price:str
    merchantName:str