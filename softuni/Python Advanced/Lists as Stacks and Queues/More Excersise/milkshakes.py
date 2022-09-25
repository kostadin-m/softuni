from collections import deque
chocolate = [int(x) for x in input().split(', ')]
cups_of_milk = deque(int(x) for x in input().split(', '))

milkshakes = 0

while chocolate and cups_of_milk and milkshakes < 5:
    choco = chocolate.pop()
    milk = cups_of_milk.popleft()
    if choco <= 0 and milk <= 0:
        continue
    if choco <= 0:
        cups_of_milk.appendleft(milk)
        continue
    if milk <= 0:
        chocolate.append(choco)
        continue
    if choco == milk:
        milkshakes +=1 
    else:
        chocolate.append(choco - 5)
        cups_of_milk.append(milk)

if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')
if chocolate:
    print('Chocolate:',", ".join(str(x) for x in chocolate))
else:
    print(f"Chocolate: empty")

if cups_of_milk:
    print(f'Milk: {", ".join(str(x) for x in cups_of_milk)}')
else:
    print('Milk: empty')