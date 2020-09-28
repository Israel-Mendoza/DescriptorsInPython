# WHAT'S NOT SUPPOSED TO BE DONE

# Storing the setter's passed value
# to an instance attribute


def print_obj_namespace(an_obj):
    print(f"{an_obj} NAMESPACE:")
    for k, v in an_obj.__dict__.items():
        print(f"{an_obj}.{k:12} -> {v}")
    print()


class IntegerValue:

    def __set__(self, instance, value):
        print(f"{instance}.stored_value = {value}")
        # Storing the value in the instance's namespace
        instance.stored_value = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, "stored_value", None)


class Point1D:

    x = IntegerValue()


class Point2D:

    x = IntegerValue()
    y = IntegerValue()


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
# but not as we imagine (because the setter is overriding the same attribute)
print_obj_namespace(p1)
print_obj_namespace(p2)
