first = set(int(x) for x in input().split())
second =set(int(x) for x in input().split())

n = int(input())


for i in range(n):
    commands= input().split()
    line = commands[1]
    command = commands[0]
    if command == 'Add':
        if line == "First":
            [first.add(int(y)) for y in commands[2:]]
        else:
            [second.add(int(y)) for y in commands[2:]]
    elif command == 'Remove':
        if line =='First':
            first = first.difference(int(y) for y in commands[2:])
        else:
            second = second.difference(int(y) for y in commands[2:])
    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
