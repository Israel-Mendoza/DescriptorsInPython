from numbers import Integral
from types import FunctionType
from typing import Any


class Property:

    def __init__(self,
                 f_get: FunctionType = None,
                 f_set: FunctionType = None,
                 f_del: FunctionType = None):
        self.get = f_get
        self.set = f_set
        self.delete = f_del

    def __set_name__(self, cls, name):
        self.property_name = name

    def __get__(self, obj, cls) -> Any:
        """Descriptor's getter method"""
        if obj is None:
            return self
        if self.get:
            return self.get(obj)
        else:
            raise AttributeError(
                f"{cls.__name__} has not implemented a getter for '{self.property_name}'")

    def __set__(self, obj, value) -> None:
        """Descriptor's setter method"""
        if self.set:
            self.set(obj, value)
        else:
            raise AttributeError(
                f"{obj.__class__.__name__} has not implemented a setter for '{self.property_name}'")

    def __delete__(self, obj) -> None:
        """Descriptor's delete method"""
        if self.delete:
            self.delete(obj)
        else:
            raise AttributeError(
                f"{obj.__class__.__name__} has not implemented a deleter for '{self.property_name}'")

    def setter(self, f_set: FunctionType = None):
        """Implements the self.set method to be called by the setter"""
        if isinstance(f_set, FunctionType):
            self.set = f_set
            self.property_name = f_set.__name__
        return self

    def deleter(self, f_del: FunctionType = None):
        """Implements the self.delete method to be called by the delete method"""
        if isinstance(f_del, FunctionType):
            self.delete = f_del
            self.property_name = f_del.__name__
        return self


class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @Property
    def name(self):
        return getattr(self, "_name")

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 1:
            setattr(self, "_name", value)
        else:
            raise ValueError("name must be a non-empty string")

    @name.deleter
    def name(self):
        delattr(self, "_name")

    @Property
    def age(self):
        return getattr(self, "_age")

    @age.setter
    def age(self, value):
        if isinstance(value, Integral) and value > 0:
            setattr(self, "_age", value)
        else:
            raise ValueError("Age must be a valid positive integer")

    @age.deleter
    def age(self):
        delattr(self, "_age")


class Point:

    def __init__(self, x: int):
        self.x = x

    x = Property()

    @x.setter
    def x(self, value):
        print("Calling the x setter!")
        if isinstance(value, Integral):
            setattr(self, "_x", value)
        else:
            raise ValueError("Point's x value must be a valid integer")

    def __repr__(self):
        return f"Point({self._x})"


person = Person("Israel", 28)
print(vars(person))
for k, v in vars(Person).items():
    print(f"{k:12}:{v}")
print("\n\n")

point = Point(10)
print(point)
point.x = -10
print(point)
try:
    print(point.x)
except AttributeError as error:
    print(error)
