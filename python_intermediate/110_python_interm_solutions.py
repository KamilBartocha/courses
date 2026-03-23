### 1)
class StrictAttributesMeta(type):
    def __new__(cls, name, bases, class_dict):
        for key in class_dict.keys():
            if not key.isupper() and not key.endswith('__'):
                raise TypeError(f"Attribute '{key}' is not uppercase in class '{name}'")
        return super().__new__(cls, name, bases, class_dict)

class JitClass(metaclass=StrictAttributesMeta):
    ATTRIBUTE_ONE = "Value"
    ATTRIBUTE_TWO = "Another Value"

class InvalidClass(metaclass=StrictAttributesMeta):
    invalid_attribute = "This will raise an error"




### 2)
class LoggingMeta(type):
    def __new__(cls, name, bases, class_dict):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, class_dict)

class MyClass(metaclass=LoggingMeta):
    pass

class AnotherClass(metaclass=LoggingMeta):
    pass










class StrictAttributesMeta(type):
    def __new__(cls, name, bases, class_dict):
        if(len(list(filter(lambda x: x.upper() != x and not x.endswith('__'), class_dict.keys()))) > 0):
            raise TypeError("attributes are not in uppercase")
        return super().__new__(cls, name, bases, class_dict)



class JitClass(metaclass=StrictAttributesMeta):
    ATTRIBUTE_ONE = "Value"
    ATTRIBUTE_TWO = "Another Value"

class InvalidClass(metaclass=StrictAttributesMeta):
    invalid_attribute = "This will raise an error"
