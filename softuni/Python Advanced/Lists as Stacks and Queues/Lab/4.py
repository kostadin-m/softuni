from collections import deque

dispenser = int(input())
command = input()
line = deque()

while not command =='End':
    if command =='Start':
        while line:
            liters_person_wants = input().split(' ')
            if liters_person_wants[0] =='refill':
                dispenser += int(liters_person_wants[1])
            elif int(liters_person_wants[0]) > dispenser:
                print(f'{line.popleft()} must wait')
            else:
                print(f'{line.popleft()} got water')
                dispenser -= int(liters_person_wants[0])    
        
    else:
        line.append(command)
    command = input()

print(f'{dispenser} liters leftyyyy')