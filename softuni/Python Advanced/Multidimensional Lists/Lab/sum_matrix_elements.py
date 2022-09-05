rows,collumns = [int(x) for x in input().split(', ')]

matrix = []
sum_of_matrix = 0
for row in range(rows):
    current_row = [int(x)for x in input().split(', ')]
    sum_of_matrix += sum(current_row)
    matrix.append(current_row)

print(sum_of_matrix)
print(matrix)