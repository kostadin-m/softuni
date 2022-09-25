matrix =[]
line = input().split('|')

for i in reversed(line):
    matrix.append(i.split())

for i in matrix:
    if i:
        print(*i,end=' ')