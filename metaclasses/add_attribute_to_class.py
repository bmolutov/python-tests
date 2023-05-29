class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['my_attribute'] = 42
        return super(MyMeta, cls).__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

print(MyClass.my_attribute)

