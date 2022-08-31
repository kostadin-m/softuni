number = input().split()
reversed = []

for i in range(len(number)):
    reversed.append(number.pop())
print(' '.join([str(x) for x in reversed]))

