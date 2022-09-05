rows = int(input())

matrix= []

for i in range(rows):
    row = [int(x)for x in input().split()]
    matrix.append(row)

def check_diagonal():
    sum_of_diagonal = 0
    for i in range(rows):
        sum_of_diagonal += matrix[i][i]
    return sum_of_diagonal

print(check_diagonal())