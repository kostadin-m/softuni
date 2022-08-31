numbers = (float(x) for x in input().split())
occ = {}
for num in numbers:
    if num in occ:
        occ[num] += 1
    else:

        occ[num] = 1
for key,value in occ.items():
    print(f'{key} - {value} times')