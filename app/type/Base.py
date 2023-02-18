from typing import Any,_SpecialGenericAlias,get_origin
import typing


class Dictionary:
    """
    A class that can be used to create a dictionary-like object with arbitrary key-value pairs.
    """
    def __init__(self, **kwargs) -> None:
        """
        Initializes the object with the given keyword arguments.
        If no arguments are given, the attributes are set to `None`.
        """
        # Iterate over the class annotations and set the attributes
        # based on the given keyword arguments
        for i, j in self.__annotations__.items() if not kwargs else kwargs.items():
            setattr(self, i, j if kwargs else None)

    def __repr__(self) -> str:
        """
        Returns a string representation of the object's dictionary.
        """
        return str(self.__dict__)

    def __setitem__(self, __name, __value) -> None:
        """
        Provides indexing and assignment functionality to the object.
        """
        setattr(self, __name, __value)

    def __getitem__(self, __name) -> Any:
        """
        Provides indexing and retrieval functionality to the object.
        """
        return self.__dict__[__name]

class StrictDictionary(Dictionary):
    """
    A subclass of `Dictionary` that enforces strict typing of the values based on the annotations of the class attributes.
    """
    def __init__(self, **kwargs) -> None:
        """
        Initializes the object with the given keyword arguments.
        If no arguments are given, the attributes are set to the default values obtained by calling the corresponding attribute functions.
        """
        if not kwargs:
            # Iterate over the class annotations and set the attributes
            # based on the default values obtained by calling the corresponding attribute functions
            for i, j in self.__annotations__.items():
                # Check if the attribute type is a function that can be called

                if type(j) is type:
                    super().__setitem__(i, j())
                elif get_origin(j):
                    super().__setitem__(i, j.__origin__())
                    
                else:
                    raise ValueError(f"can't assign {type(j)} data. Illegal Value.")
        else:
            # Call the superclass constructor to set the attributes based on the given keyword arguments
            super().__init__(**kwargs)
    def validate(self,__name,__value):
        pass
    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        Overrides the superclass `__setattr__` method to perform type checking before assignment.
        If the value to be assigned is not of the expected type, a `TypeError` is raised.
        """
        expected_type=self.__annotations__[__name] 
        
            # Checking if expected_type is of Typing Class than converting it into it's base class
        if get_origin(expected_type):
            expected_type=get_origin(expected_type)
        
        # Raise error if the given value is not of the expected type
        if not type(__value) == expected_type:
            raise TypeError(
                f'{__name} key has a value {__value} which is of type {type(__value)}. {expected_type} expected.')
        
        super().__setattr__(__name, __value)


    def __setitem__(self, __name, __value) -> None:
        """
        Overrides the superclass `__setitem__` method to perform type checking before assignment.
        If the value to be assigned is not of the expected type, a `TypeError` is raised.
        """
        expected_type=self.__annotations__[__name]

        # verifying for Typing types
        if get_origin(expected_type):
            expected_type=expected_type.__origin__

        if not type(__value) == expected_type:
            raise TypeError(
                f'{__name} key has a value {__value} which is of type {type(__value)}. {self.__annotations__[__name]} expected.')
        else:
            super().__setitem__(__name, __value)
