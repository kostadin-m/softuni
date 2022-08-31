n = input()
stacked_numbers = []
for _ in range(n):
    line = input().split()
    if line[0] =='1':
        stacked_numbers.append(int(line[1]))
    elif line[0] == '2':
        if len(stacked_numbers) > 0:
            stacked_numbers.pop()
    elif line[0] == '3':
        print(max(stacked_numbers))
    elif line[0] == '4':
        print(min(stacked_numbers))
while stacked_numbers:
    last = stacked_numbers.pop()
    if stacked_numbers:
        print(last,end=', ')
    else:
        print(last)


