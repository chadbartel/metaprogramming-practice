class Descriptor:
    def __init__(self, name=None):
        self.name = name
        # This is capturing the KEY of a dict

    def __get__(self, instance, cls):
        # instance: is the instance being manipulated
        # e.g. Stock instance or MasterClass instance
        print("Get", self.name)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("Set", self.name, value)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print("Delete", self.name)
        del instance.__dict__[self.name]




# Alternatively, we could do the following:

class Typed(Descriptor):
    ty = object # Expected type
    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError("Expected %s" % self.ty)
        super().__set__(instance, value)

class Integer(Typed):
    ty = int

class Float(Typed):
    ty = float

class String(Typed):
    ty = str
    
# Related example:
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

class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
