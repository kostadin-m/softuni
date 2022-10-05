class MustContainAtSymbolError(Exception):
    ...


class NameTooShortError(Exception):
    ...


class InvalidDomainError(Exception):
    ...


valid = ['.com', '.bg', '.org', '.net']
while True:
    try:
        name, domain = input().split('@')
    except:
        raise MustContainAtSymbolError('Email must contain @')
    
    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')
    
    for dom in valid:
        if domain.endswith(dom):
            break
    else:
        raise InvalidDomainError('Domain must be one of the following: ', (', '.join(str(x) for x in valid)))
    
    print('Email is valid')
