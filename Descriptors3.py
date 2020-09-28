class Descriptor:

    def __init__(self, descriptor_value):
        self.value = descriptor_value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        print(f"Instance: {instance}")
        print(f"Value: {value}")
        instance.value = value


class Person:

    race = Descriptor("Black")

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Anthony Griffy", 30)
print("INITIAL PERSON NAMESPACE: ")
for k, v in vars(Person).items():
    print(f"{k:12} - {v}")
print()
Person.race = "White"
print("FINAL PERSON NAMESPACE: ")
for k, v in vars(Person).items():
    print(f"{k:12} - {v}")
