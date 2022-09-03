from collections import deque


main_colors = ['red','yellow','blue']
secondary_color = ["orange", "purple", "green"]

needed_for_secondary = {
    'orange' : ['red', 'yellow'],
    'purple' : ['red', 'blue'],
    'green' : ['yellow', 'blue'],
}

found_colors = []

line = deque(input().split())


while line:

    first = line.popleft()
    second = line.pop() if line else ''
    result  = first+second 
    if result in main_colors or result in secondary_color:
        found_colors.append(result)
        continue
    result = second + first
    if result in main_colors or result in secondary_color:
        found_colors.append(result)
        continue
       
    first = first[:-1]
    second = second[:-1]
    
    if first:
        line.insert(int(len(line) // 2), first)
    if second:
        line.insert(int(len(line) // 2), second)

result = []


for color in found_colors:
    if color in main_colors:
        result.append(color)
    else:
        
        is_valid = True
        for required in needed_for_secondary[color]:
            if required not in found_colors:
                is_valid = False
                break
        if is_valid:
            result.append(color)


print(result)