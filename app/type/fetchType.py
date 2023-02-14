from enum import Enum

"""
This class defines the Enum 'fetchType'.

The enum has three constant fields - VIDEO, GENERAL and USER.
VIDEO, GENERAL and USER constants respectively hold values of 1,2 and 3.
"""
class fetchType(Enum):
    VIDEO = 1
    GENERAL = 2
    USER=3
    