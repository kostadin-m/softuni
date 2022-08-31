n= int(input())
unique_names = set()

for names in range(n):
    name = input()
    unique_names.add(name)
    
print('\n'.join(str(x) for x in unique_names))
