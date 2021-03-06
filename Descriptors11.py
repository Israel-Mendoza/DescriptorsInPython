class ValidString:

    def __init__(self, min_length=0, max_length=25):
        """
        Defines the minimum and maximum length
        of the string we wanto to validate.
        """
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner_class, property_name):
        """
        Set name descriptor method.
        Stores the class attribute name in self.property_name.
        """
        self.property_name = property_name

    def __get__(self, instance, owner):
        """
        Descriptor getter method.
        Returns the descriptor if called from the class,
        or the value assigned to the instance attribute, 
        if called from the instance, using the instance's
        __dict__ attribute, otherwise we would end up in 
        a recursive loop by calling the __get__ again.
        """
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)

    def __set__(self, instance, value):
        """
        Descriptor setter method.
        Checks if the value is a valid string, as defined by the 
        self.check_valid_string method.
        If it is, stores the value in the instance's namespace,
        with the property name itself, using the instance __dict__
        attribute, otherwise we would end up in a recursive loop
        by calling the __set__ again.
        """
        if self.check_valid_string(value):
            instance.__dict__[self.property_name] = value
        else:
            raise ValueError(f"{self.property_name} must be a string between "
                             f"{self.min_length} and {self.max_length} characters long!")

    def check_valid_string(self, a_string: str):
        if isinstance(a_string, str):
            return self.min_length <= len(a_string) <= self.max_length
        else:
            raise ValueError(f"{self.property_name} must be a valid string!")


class Person:
    # Descriptors are instantiated at compile time
    first_name = ValidString()
    last_name = ValidString()

    def __init__(self, age):
        self.__age = age


p = Person(28)
p_hex_address = hex(id(p)).upper()
print(f"p address: {p_hex_address}")
# p address: 0X3190748
print()

p.first_name = "Israel"
p.last_name = "Mendoza"
print(vars(p))
# {'_Person__age': 28, 'first_name': 'Israel', 'last_name': 'Mendoza'}
