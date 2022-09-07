primary_sum = 0
secondary_sum =0

rows = int(input())
col = rows 
matrix = []

for i in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)
for i in range(rows):

    primary_sum += matrix[i][i]

    secondary_sum += matrix[i][rows - 1 - i]   


print(abs(primary_sum - secondary_sum))