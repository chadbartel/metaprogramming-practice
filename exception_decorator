def handle_exceptions(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Exception:", e)
            return 'n/a'
    return inner

@handle_exceptions
def divide(x, y):
        return x / y

print(divide(8, 0))
