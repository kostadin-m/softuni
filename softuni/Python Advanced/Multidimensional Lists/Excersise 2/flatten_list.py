from collections import deque
matrix = []
line = deque(input().split('|'))

for i in reversed(line):
    matrix.append(i.split())

for i in matrix:
    print(*i,end=' ')