sets = [int(x) for x in input().split()]
set1 = set()
set2 = set()

for i in range(int(sets[0])):
    set1.add(int(input()))
for c in range (int(sets[1])):
    set2.add(int(input()))

final = [str(x) for x in (set1 & set2)]

print('\n'.join(final))