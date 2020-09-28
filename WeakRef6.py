from weakref import ref


class ValidString:

    def __init__(self, min_length=0, max_length=25):
        self._min_length = min_length
        self._max_length = max_length
        self._data = dict()

    def __get__(self, instance, owner_class) -> str:
        """
        Descriptor getter method.
        Returns the self._data dictionary if called from a class.
        Returns the corresponding instance value if called from an instance.
        """
        if instance is None:
            return self._data
        address = id(instance)
        return self._data[address][0]

    def __set__(self, instance, value: str):
        """
        Descriptor setter method.
        Creates/update entry in the self._data dictionary. 
            Key -> Instance memory address.
            Value -> tuple(value, weak_ref to instance object)
        """
        if self._check_string(value):
            address = id(instance)
            intance_weak_ref = ref(instance, self._clear_data_entry)
            self._data[address] = (value, intance_weak_ref)
        else:
            raise ValueError(f"String must be between {self._min_length} "
                             f"and {self._max_length} characters long!")

    def _check_string(self, a_string: str) -> bool:
        """Checks whether the passed string is within the string limits"""
        length = len(a_string)
        return self._min_length < length < self._max_length

    def _clear_data_entry(self, weak_ref_obj):
        """Deletes the entry from self._data once the object is destroyed"""
        target_address = id(weak_ref_obj)
        for key, value in self._data.items():
            if id(value[1]) == target_address:
                del self._data[key]
                break


class Person:

    __slots__ = "__weakref__",

    first_name = ValidString(1, 20)
    last_name = ValidString(1, 20)


p1 = Person()
p1.first_name = "Israel"
p1.last_name = "Mendoza"

print(p1.first_name, p1.last_name)

try:
    p1.first_name = ""
except ValueError as error:
    print(error)
