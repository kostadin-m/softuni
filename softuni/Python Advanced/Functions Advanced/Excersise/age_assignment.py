def age_assignment(*args,**kwargs):
    result = ''
    for name in sorted(args):
        age = kwargs[name[0]]
        result +=  (f'{name} is {age} years old.\n')
    return result




