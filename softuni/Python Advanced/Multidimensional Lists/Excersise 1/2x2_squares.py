rows,coll = [int(x) for x in input().split()]

matrix = []
count  =0
for i in range(rows):
    row  = input().split()
    matrix.append(row)

for i in range(rows -1 ):
    for x in range(coll- 1):
        if  matrix[i][x] == matrix[i+ 1][x] == matrix[i][x+ 1] ==matrix[i+ 1][x+ 1]:
            count +=1
print(count)