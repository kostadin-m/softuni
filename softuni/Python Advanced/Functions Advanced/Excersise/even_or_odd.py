def even_odd(*args,):
    parity = 0 if args[-1] =='even' else 1
    result = ([x for x in args[:-1] if x % 2 == parity])
    return result

