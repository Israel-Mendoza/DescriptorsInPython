import weakref
from ctypes import c_long


def get_ref_count(address: int) -> int:
    return c_long.from_address(address).value


class Person:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person('{name}')"


p1 = Person("Israel")
p1_address = id(p1)
p1_hex_address = hex(p1_address).upper()

print(f"Reference count on {p1_hex_address}: {get_ref_count(p1_address)}")
print()

p2 = p1
print(f"Reference count on {p1_hex_address}: {get_ref_count(p1_address)}")
print()

weak1 = weakref.ref(p1)
print(f"Reference count on {p1_hex_address}: {get_ref_count(p1_address)}")
print()

print(f"What is 'weak1' pointing to then? {weak1}")
print()

p3 = weak1()
print(f"Reference count on {p1_hex_address}: {get_ref_count(p1_address)}")
print()

print("Deleting p3.")
del p3
print(f"Reference count on {p1_hex_address}: {get_ref_count(p1_address)}")
print()

print("Deleting p1 and p2.")
del p1, p2
print(f"Reference count on {p1_hex_address}: {get_ref_count(p1_address)}")
print()

print(f"What is weak1 pointing to? {weak1} --> {weak1()}")
