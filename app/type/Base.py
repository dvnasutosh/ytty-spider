from typing import Any

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
                if type(j) != type:
                    raise ValueError(f"can't assign {type(j)} data. Illegal Value")
                else:
                    super().__setitem__(i, j())
        else:
            # Call the superclass constructor to set the attributes based on the given keyword arguments
            super().__init__(**kwargs)

    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        Overrides the superclass `__setattr__` method to perform type checking before assignment.
        If the value to be assigned is not of the expected type, a `TypeError` is raised.
        """
        if not type(__value) == self.__annotations__[__name]:
            raise TypeError(
                f'{__name} key has a value {__value} which is of type {type(__value)}. {self.__annotations__[__name]} expected.')
        else:
            return super().__setattr__(__name, __value)

    def __setitem__(self, __name, __value) -> None:
        """
        Overrides the superclass `__setitem__` method to perform type checking before assignment.
        If the value to be assigned is not of the expected type, a `TypeError` is raised.
        """
        if not type(__value) == self.__annotations__[__name]:
            raise TypeError(
                f'{__name} key has a value {__value} which is of type {type(__value)}. {self.__annotations__[__name]} expected.')
        else:
            super().__setitem__(__name, __value)
