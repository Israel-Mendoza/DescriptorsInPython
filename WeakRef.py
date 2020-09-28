from ctypes import c_long


def get_ref_count(address: int) -> int:
    return c_long.from_address(address).value


class Person:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person('{name}')"


p1 = Person("Israel")
p2 = p1
obj_address = id(p1)
obj_hex_address = hex(obj_address)

print(f"id(p1) = {hex(id(p1))}")
print(f"id(p2) = {hex(id(p2))}")
print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
print()

# Deleting p1
print(f"Deleting p1")
del p1
print()

print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
print()

# Deleting p1
print(f"Deleting p2")
del p2
print()

# The reference count is now meaningless
print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
