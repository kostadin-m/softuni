from collections import deque

n = int(input())
truck_tour = deque()
for i in range(n):
    trucks = input().split()
    truck_tour.append(trucks)

for attempt in range(n):
    tank = 0
    failed = False
    for pump,distance in truck_tour:
        tank += int(pump)
        
        
        if int(tank) < int(distance):
            failed = True
            break
    if failed:
        truck_tour.rotate(-1)
    else:
        print(attempt)
        break
    
    