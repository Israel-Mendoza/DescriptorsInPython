from weakref import ref
from ctypes import c_long


def get_ref_count(address: int) -> int:
    return c_long.from_address(address).value


class IntegerValue:

    def __init__(self):
        """
        Initializes an empty dictionary where the
        instance information and values will be stored.
        """
        self.values = {}

    def __get__(self, instance, type):
        """
        Descriptor getter method.
        Returns the descriptor instance if called from a class.
        Returns the assigned value if called from an instance.
        """
        if instance is None:
            return self
        address = id(instance)
        return self.values[address][1]

    def __set__(self, instance, value):
        """
        Descriptor setter method.
        Stores the value in the descriptor instance's value dictionary.
        The key will be the instance memory address.
        The value will be a tuple containing
            index 0: a weak_ref object pointing to the instance
                    and a callback method to be called when the instance
                    is elligible for garbage collection.
            index 1: The value of the instance, to be obtained by the 
                    getter method.
        """
        address = id(instance)
        self.values[address] = (ref(instance, self._remove_item), value)

    def _remove_item(self, weak_ref_obj):
        """
        Intended as a callback method.
        When called, iterating through the self.values dictionary,
        looking for the key-value pair where the passed weak_ref
        object is.
        Once found, it deletes the dictionary entry.
        """
        for k, v in self.values.items():
            if id(weak_ref_obj) == id(v[0]):
                del self.values[k]
                break


class Point1D:

    x = IntegerValue()

    def __eq__(self, other):
        """
        Implementing the = operator for the class.
        Also, making sure this is not a hashable object.
        """
        if isinstance(other, self.__class__):
            return self.x == other.x
        else:
            return NotImplemented

    @classmethod
    def show_x_descriptor(cls):
        print(f"{cls.__name__}.x's values:")
        for k, v in cls.x.values.items():
            print(f"Address {hex(k).upper()}:{v}")


p1 = Point1D()
p2 = Point1D()

p1.x = 10
p2.x = 20

Point1D.show_x_descriptor()
print()

del p1
print()

Point1D.show_x_descriptor()
print()

del p2
print()

Point1D.show_x_descriptor()
print()
