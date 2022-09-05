
rows,collumns = (int(x) for x in input().split(', '))


matrix =[]
for i in range(rows):
    matrix.append([int(x) for x in input().split()])


for collumn in range(collumns):
    sum_of_collumns = 0
    for row in range(rows):
        sum_of_collumns += matrix[row][collumn]
    print(sum_of_collumns)

