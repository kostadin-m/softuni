def func_executor(*args):
    result =[]
    for function, parameters in args:
        result.append(f'{function.__name__} - {function(*parameters)}')
    return ('\n'.join(result))

