def _make_init(fields):
    '''
    Give a list of field names, make an __init__ method
    :param fields:
    :return:
    '''
    code = 'def __init__(self, %s):\n' % ', '.join(fields)
    for name in fields:
        code += '   self.%s = %s\n' % (name, name)
    return code

print(_make_init(['name', 'shares', 'price']))
