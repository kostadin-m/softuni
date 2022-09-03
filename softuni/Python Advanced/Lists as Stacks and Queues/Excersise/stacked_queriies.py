n = int(input())
stacked_numbers = []
for _ in range(n):
    line = input().split()
    command = line[0]
    if command =='1':
        stacked_numbers.append(int(line[1]))
    elif command == '2' and stacked_numbers:
        stacked_numbers.pop()
    elif command == '3'and stacked_numbers:
        print(max(stacked_numbers))
    elif command == '4' and stacked_numbers:
        print(min(stacked_numbers))
while stacked_numbers:
    last = stacked_numbers.pop()
    if stacked_numbers:
        print(last,end=', ')
    else:
        print(last)


