n = int(input())

even_set = set()
odd_set= set()

for i in range(1, n + 1):
    total_value = 0
    name = sum([ord(x) for x in  input()]) / i
    
    if int(name) % 2 ==0:
        even_set.add(int(name))
    else:
        odd_set.add(int(name))

if sum(odd_set) < sum(even_set):
    final = odd_set ^ even_set
elif sum(odd_set) > sum(even_set):
    final = odd_set - even_set
else:
    final = odd_set | even_set

print(*final,sep=', ')