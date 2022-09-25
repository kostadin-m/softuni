rows = int(input())
matrix = [[int(x) for x in input().split(', ')]for _ in range(rows)]
final  ={
    'primary':[],
    'secondary':[]
}

for i in range(rows):
    final['primary'].append(matrix[i][i])
    final['secondary'].append(matrix[i][rows - 1 - i])

print(f"Primary diagonal: {', '.join([str(x) for x in final['primary']])}. Sum: {sum(final['primary'])}")
print(f"Secondary diagonal: {', '.join([str(x) for x in final['secondary']])}. Sum: {sum(final['secondary'])}")