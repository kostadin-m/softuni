n = int(input())

unique_chemicals = set()

for i in range(n):
    command = input().split()
    unique_chemicals.union(command)

for x in unique_chemicals:
    print(x)