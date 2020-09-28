def print_obj_namespace(an_obj):
    print(f"{an_obj} NAMESPACE:")
    for k, v in an_obj.__dict__.items():
        print(f"{an_obj}.{k:12} -> {v}")
    print()


class IntegerValue:

    def __init__(self, name: str):
        """
        Initializing the name of the instance attribute the descriptor
        will be getting from and setting to.
        The name will be preceeded by an underscore.
        """
        self.storage_name = f"_{name}"

    def __set__(self, instance, value):
        """
        Sets the passed value to the instance attribute,
        which name is contained in self.storage_name
        """
        print(f"{instance}.{self.storage_name} = {value}")
        instance.__dict__[self.storage_name] = value

    def __get__(self, instance, owner):
        """
        Gets the the instance attribute,
        which name is contained in self.storage_name
        """
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)


class Point1D:

    x = IntegerValue("x")


class Point2D:

    x = IntegerValue("x")
    y = IntegerValue("y")


p1 = Point1D()
p2 = Point1D()

# p1 and p2's namespaces are now empty
print_obj_namespace(p1)
print_obj_namespace(p2)

p1.x = 10
p2.x = 20
print()

# p1 and p2's namespaces are populated by the setter
print_obj_namespace(p1)
print_obj_namespace(p2)

# USING Point2D class
print("*" * 50)

p1 = Point2D()
p2 = Point2D()

# p1 and p2's namespaces are now empty
print_obj_namespace(p1)
print_obj_namespace(p2)

# Using the setters to set the instance's attribute
p1.x = 100
p1.y = 200
p2.x = 1000
p2.y = 2000
print()

# p1 and p2's namespaces are populated by the setter
print_obj_namespace(p1)
print_obj_namespace(p2)
