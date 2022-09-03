from collections import deque


cars= deque()
duration_green_light = int(input())
free_window = int(input())
safe_count = 0
crash = False

command = input()

while command != 'END':
    if command == 'green':
        duration = duration_green_light
    
    
        while cars and duration > 0:
            car = cars.popleft()
            if duration + free_window >= len(car):
                if duration >= len(car):
                    duration -=len(car)
                    safe_count +=1
                else:
                    safe_count +=1
                    break
            else:
                full_time = duration + free_window
                print(f'A crash happened!\n{car} was hit at {car[full_time]}.')
                crash = True
                break
    else:
        cars.append(command)   
    if crash:
        break        
    command = input()
if not crash:
    print(f'Everyone is safe.\n{safe_count} total cars passed the crossroads.')



    


