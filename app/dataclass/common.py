import datetime
from urllib.parse import parse_qsl, urlparse
from app.dataclass.Base import StrictDictionary
import re

class img(StrictDictionary):
    url:str
    width:int
    height:int

class strList(list):
    def __init__(self,args:list=list()):
        if not all([isinstance(i, str) for i in args]):
            raise ValueError('keywordList will need to have "str" type items only')
        super().__init__(args)


class dateInt(int):
    
    """
        A subclass of int that stores a date in an integer format that represents 
        the date as the number of milliseconds since the Unix epoch (January 1, 1970).
        
        Accepts date strings in the following formats:
        - 'YYYY-MM-DD'
        - 'MMM DD, YYYY'
        - 'YYYY-MM-DDTHH:MM:SSZ'
        - 'YYYY-MM-DDTHH:MM:SS.sssZ'
        - 'YYYY-MM-DDTHH:MM:SS±HH:MM'
        - 'YYYY-MM-DDTHH:MM:SS.sss±HH:MM'
        
        Examples:
        - '2023-03-10'
        - 'Nov 17, 2012'
        - '2023-03-10T14:00:08+00:00'
        - '2023-03-10T14:00:08.999Z'
        - '2023-03-10T14:00:08-07:00'
        - '2023-03-10T14:00:08.999-07:00'
    """
    date_formats = [
        ('%Y-%m-%d', re.compile(r'\d{4}-\d{2}-\d{2}$')),
        ('%Y-%m-%dT%H:%M:%S.%fZ', re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z$')),
        ('%Y-%m-%dT%H:%M:%S.%f%z', re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}$')),
        ('%Y-%m-%dT%H:%M:%SZ', re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$')),
        ('%Y-%m-%dT%H:%M:%S%z', re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}$')),
        ('%b %d, %Y', re.compile(r'[a-zA-Z]{3} \d{2}, \d{4}$')),
    ]
    
    def __new__(cls, date_str=None, default_value=-1):
        """
        Creates a new instance of the class with the date_str argument. The argument
        should be a string in one of the accepted datetime formats. The method converts
        the string into a datetime object and then into an integer representing the 
        number of milliseconds since the Unix epoch. The integer is then used to create
        a new instance of the class.
        
        :param date_str: A string representing a date in an accepted datetime format.
        :param default_value: The default value to return if no date string is provided.
        :return: A new instance of the DateInt class.
        """
        if date_str is None:
            return super().__new__(cls, default_value)
        
        # Define accepted datetime formats
        for date_format, regex in cls.date_formats:
            if regex.match(date_str):
                date_obj = datetime.datetime.strptime(date_str, date_format)
                timestamp = int(date_obj.timestamp())
                return super().__new__(cls, timestamp)
        
        raise ValueError("Invalid date string format")

        
    def todatetime(self):
        """
        Converts the internally stored integer timestamp into a datetime object
        and returns it.
        
        :return: A datetime object representing the stored date.
        """
        return datetime.datetime.fromtimestamp(self)

class publishTime(StrictDictionary):
    publishedTimeText:str
    since:float
    
class strbool(int):
    def __new__(cls, value=bool()):
        if isinstance(value, str):
            if value.lower() == "true":
                return super().__new__(cls, 1)
            elif value.lower() == "false":
                return super().__new__(cls, 0)
        return super().__new__(cls, value)

class url(str):
    def __new__(cls, url_string=str()):
        if not url_string:
            obj=super().__new__(cls,url_string)
            obj.query_params=dict()
            return obj
        if not isinstance(url_string, str):
            raise TypeError(f"Expected str, but got {type(url_string).__name__}")
        parsed_url = urlparse(url_string)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError("Invalid URL")
        obj = super().__new__(cls, url_string)
        obj.query_params = dict(parse_qsl(parsed_url.query))
        return obj

    @staticmethod
    def is_valid_url(url_string):
        regex = re.compile(
            r"^(?:http|ftp)s?://"  # http:// or https:// or ftp:// or ftps://
            # domain...
            r"(?:[A-Za-z0-9]+(?:[-._][A-Za-z0-9]+)*\.)+[A-Za-z]{2,}"
            # port...
            r"(?::\d{2,5})?"
            # path...
            r"(?:/.*)?$",
            re.IGNORECASE
        )
