name = list(input())
reversed = []
for i in range (len(name)):
    reversed.append(name.pop())
print(''.join(reversed))



