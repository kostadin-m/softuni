from collections import deque
bees = deque(int(i) for i in input().split())
nectar = [int(i) for i in input().split()]
operators = deque(input().split())
honey = 0
op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '/': lambda x, y: x / y,
      '*': lambda x, y: x * y,}


while bees and nectar:
    bee = bees[0]
    nect = nectar.pop()
    if bee > nect:
        continue
    operator = operators.popleft()
    if operator == '/':
        if nect > 0:
            honey += abs(op[operator](bees.popleft(),nect))
        else:
            continue
    else:
        honey += abs(op[operator](bee,nect))
print(f'Total honey made: {honey}')

if bees:
    print(f'Bees left: {", ".join(str(x) for x in bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')
