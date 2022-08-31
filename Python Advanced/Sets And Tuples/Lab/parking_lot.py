n = int(input())
parking_lot = set()

for i in range(n):
    command = input().split(', ')
    if command[0] =='IN':
        parking_lot.add(command[1])
    elif command[0] =='OUT':
        parking_lot.remove(command[1])

if len(parking_lot) == 0:
    print(f'Parking Lot is Empty')

else:
    print('\n'.join(parking_lot))

