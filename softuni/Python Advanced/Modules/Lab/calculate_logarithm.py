from math import log

n = int(input())
base = input()

if base == 'natural':
    print(f'{log(n):.2}')
else:
    print(f'{log(n, int(base)):.2f}')