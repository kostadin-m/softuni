def rectangle(*args):
    try:
        
        def area(args):
            result = 1
            for x in args:
                result *= x
            return result

        def perimeter(args):
            result = 0
            for y in args:
                result += y + y
            return result
        return (f'Rectangle area: {area(args)}')+\
                '\n' +\
                f'Rectangle perimeter: {perimeter(args)}'
    
    except:
        return ('Enter valid values!')
