from pydantic import BaseModel

class DynamicMembers(BaseModel):
    """
    A class that allows creation and assignment of member data using square bracket notation.

    This class inherits from `pydantic.BaseModel` and automatically generates the `__fields__` attribute based on the
    field annotations in the class definition. The class also provides the ability to assign values to the members using
    square bracket notation, and it raises a `KeyError` if you try to assign a value to a member that doesn't exist.
    """
    def __init__(self):
        """
        Initialize an instance of the `DynamicMembers` class.

        This method creates an empty dictionary `data` and sets the value of each key in `data` to `None` based on the field
        names and types defined in the `__fields__` attribute of the class.
        """
        self.data = {}
        for key, value in self.__fields__.items():
            self.data[key] = None

    def __setitem__(self, key, value):
        """
        Set the value of a member data item.

        This method allows you to assign a value to a member using square bracket notation, and it raises a `KeyError` if
        you try to assign a value to a member that doesn't exist. The method also raises a `TypeError` if the value being
        assigned is not of the correct type.
        """
        if key in self.__fields__:
            if isinstance(value, self.__fields__[key].type_):
                self.data[key] = value
            else:
                raise TypeError(f"Expected value of type {self.__fields__[key].type_}, got {type(value)}")
        else:
            raise KeyError(f"{key} is not a valid member")
