import inspect
from inspect import Parameter, Signature

def make_signature(names):
    return Signature(
        Parameter(name,
                  Parameter.POSITIONAL_OR_KEYWORD)
        for name in names)

class Structure:
    # Define generalized init method
    # This ensures we are entering all fields have values
    # and we can support keyword args or positional
    __signature__ = make_signature([])
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(
            *args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


# Simple example
class Stock(Structure):
    __signature__ = make_signature(['name', 'shares', 'price'])

class Point(Structure):
    __signature__ = make_signature(['x', 'y'])

s = Stock('GOOG', 100, 490.1)
print(s.name)
print(s.shares)
s = Stock(name='GOOG', price=490.1, shares=100) # kwargs
s = Stock('GOOG', 100)  # throws error -> not enough args

print(inspect.signature(Stock))




# Alternatively, we could add signatures through decorators

def add_signature(*names):
    def decorate(cls):
        cls.__signature__ = make_signature(names)
        return cls
    return decorate

# Example
@add_signature('name', 'shares', 'price')
class Stock(Structure):
    pass

@add_signature('x', 'y')
class Point(Structure):
    pass




# Lastly, we could do the same thing through setting a metaclass
class StructMeta(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name,
                                 bases, clsdict)
        sig = make_signature(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj

class Structure(metaclass=StructMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(
            *args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

# Example
class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    
class Point(Structure):
    _fields = ['x', 'y']
