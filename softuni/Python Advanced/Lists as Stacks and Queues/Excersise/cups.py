from collections import deque

cups = deque([int(i) for i in input().split()])
bottles_stack = [int(x) for x in input().split()]
wasted_water = 0


while cups and bottles_stack:
    cup = cups.popleft()
    bottle = bottles_stack.pop()
    if cup > bottle:
        cup -= bottle
        cups.appendleft(cup)
    else:
        wasted_water += abs(cup - bottle)
if not cups:
    print('Bottles:',' '.join([str(y) for y in bottles_stack]))
    print(f'Wasted litters of water: {wasted_water}')
else:
    print('Cups:',' '.join([str(y) for y in cups]))
    print(f'Wasted litters of water: {wasted_water}')


