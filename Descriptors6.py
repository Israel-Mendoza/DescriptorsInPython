class IntegerValue:

    def __set__(self, intance, value):
        # A message gets printed when the setter is called
        print(f"__set__ called!!!")

    def __get__(self, instance, owner):
        # A message describing which object called the attribute
        if instance is None:
            print(f"__get__ called from class {owner}!")
        else:
            print(f"__get__ called from the class instance {instance}!")


class Point2D:
    x = IntegerValue()
    y = IntegerValue()

    def __init__(self, name):
        self.name = name


p = Point2D("A Point")
Point2D.x
p.x
p.x = 10
