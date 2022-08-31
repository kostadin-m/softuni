from collections import deque
food = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))

while orders:
    placed_order = orders[0]
    if placed_order > food:
        break
    food -=placed_order
    orders.popleft()

if orders:
    print(f'Orders left: {" ".join([str(i) for i in orders])}')
else:
    print(f'Orders complete')