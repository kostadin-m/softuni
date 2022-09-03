parenthasis = input()
parethasis_list = []

balanced = True
for character in parenthasis:
    if character in '({[':
        parethasis_list.append(character)
    else:
        if parethasis_list:
            last_opening_bracket = parethasis_list.pop()
            if f'{last_opening_bracket}{character}'  not in '()[]{}':
                balanced = False
                break
        else:
            balanced = False    
            break       
if balanced:
    print('YES')
else:
    print('NO')

