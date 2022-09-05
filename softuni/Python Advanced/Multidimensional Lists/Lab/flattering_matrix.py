rows = int(input())

flat_matrix= []

for i in range(rows):
    row = input().split(', ')
    flat_matrix.extend(row)

print(f'[{", ".join(str(x) for x in flat_matrix)}]')