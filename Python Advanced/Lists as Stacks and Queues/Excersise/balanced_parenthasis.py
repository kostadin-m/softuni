parenthasis = input()
parethasis_list = []

balanced = False
for character in parenthasis:
    if character in '({[':
        parethasis_list.append(character)
    else:
        last_opening_bracket = parethasis_list.pop()
        if f'{last_opening_bracket}{character}' in '[]{}()':
            balanced = True

if balanced:
    print('YES')
else:
    print('BLA')


