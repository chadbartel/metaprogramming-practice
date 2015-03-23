class Structure:
    _fields = []
    # Define generalized init method
    def __init__(self, *args):
        for name, val in zip(self.__class__._fields, args):
            setattr(self, name, val)

# Simple example
class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

class Address(Structure):
    _fields = ['hostname', 'port']

s = Stock('GOOG', 100, 490.1)
print(s.name)
print(s.shares)
print(s.price)

# Need to check for empty args
# We can't use keyword args if we do this

# Ex: Can't do s=Stock(name='GOOG')
