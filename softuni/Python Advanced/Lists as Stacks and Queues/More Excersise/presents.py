from collections import deque
presents = {
    400: 'Bicycle',
    300: 'Teddy bear',
    250: 'Wooden train',
    150: 'Doll',
}

presents_crafted = {}


materials = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())


while materials and magic_values:
    box = materials.pop()
    magic = magic_values.popleft()
    
    result = box * magic
    
    if result in presents:
        toy = presents[result]
        if toy not in presents_crafted:
            presents_crafted[toy] = 1
        else:
            presents_crafted[toy] += 1
    elif result < 0:
        materials.append(box + magic)
    elif result > 0:
        materials.append(box + 15)
    else:
        if magic == 0 and box == 0:
            continue
        if magic == 0:
            materials.append(box)
        else:
            magic_values.appendleft(magic)

        

if ('Doll' in presents_crafted and 'Wooden train' in presents_crafted) or\
    ('Teddy bear' in presents_crafted and 'Bicycle' in presents_crafted):
    print(f'The presents are crafted! Merry Christmas!')
else:
   print(f'No presents this Christmas!')
if materials:
    print(f'Materials left: {", ".join(str(x) for x in reversed(materials))}')    
if magic_values:
    print(f'Magic left: {", ".join(str(x) for x in magic_values)}')

for name,count in sorted(presents_crafted.items()):
    print(f'{name}: {count}')