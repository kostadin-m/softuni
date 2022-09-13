from functools import reduce
op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '/': lambda x, y: x/y,
      '*': lambda x, y: x * y,}

def operate(operator,*args):
    if operator in ('+' or '-'):
        result = 0
    else:
        result = 1
    return  reduce(op[operator],args)





