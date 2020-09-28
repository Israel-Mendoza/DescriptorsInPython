# Using a dictionary within the descriptor's instance
# to store the instance's attributes.
# The instance is the key, the value, the value.

from ctypes import c_long


def get_ref_count(address: int):
    return c_long.from_address(address).value


def print_obj_namespace(an_obj):
    print(f"{an_obj} NAMESPACE:")
    for k, v in an_obj.__dict__.items():
        print(f"{an_obj}.{k:12} -> {v}")
    print()


class IntegerValue:

    def __init__(self):
        """
        Initializing an empty dict where the intances will be keys,
        and the set values, the values.
        """
        self.values = {}

    def __set__(self, instance, value):
        print(f"Adding/Updating instance's value in descriptor.")
        self.values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(f"Getting instance's value from descriptor")
        return self.values.get(instance, None)


class Point1D:

    x = IntegerValue()

    __slots__ = ("name",)

    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def show_x_descriptor(self):
        for k, v in self.__class__.x.values.items():
            print(f"{k} -> {v}")


p1 = Point1D("p1")
p2 = Point1D("p2")

p1_address = id(p1)
print(f"p1 reference count: {get_ref_count(p1_address)}")

p1.x = 10
p2.x = 20
p1.x
p2.x

# Repeated info, because there is a single descriptor
# object holding the values:
p1.show_x_descriptor()
p2.show_x_descriptor()
print()

# Memory caveats. Possible memory leaks.

p1_address = id(p1)
print(f"p1 memory address: {hex(p1_address).upper()}")
print(f"p1 reference count: {get_ref_count(p1_address)}")
print(f"Is p1 in the global scope? {'p1' in globals()}")
print(f"Deleting p1 from the global scope.")
del p1
print(f"Is p1 in the global scope still? {'p1' in globals()}")
print(f"p1 reference count: {get_ref_count(p1_address)}")
print("Where is this reference to this object?")
print(f"Address in the descriptor's dict: "
      f"{hex(id(list(Point1D.x.values.keys())[0])).upper()}")
