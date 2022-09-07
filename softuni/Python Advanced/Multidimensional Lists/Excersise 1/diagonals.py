rows = int(input())
col = rows 
matrix = []
final  ={
    'primary':[],
    'secondary':[]
}

for i in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)


for i in range(rows):
    final['primary'].append(matrix[i][i])
    final['secondary'].append(matrix[i][rows - 1 - i])

print(f"Primary diagonal: {', '.join([str(x) for x in final['primary']])}. Sum: {sum(final['primary'])}")
print(f"Secondary diagonal: {', '.join([str(x) for x in final['secondary']])}. Sum: {sum(final['secondary'])}")