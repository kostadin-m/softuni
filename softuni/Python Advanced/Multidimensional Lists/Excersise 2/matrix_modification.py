def is_valid(row,col,rows,cols):
    return 0 <=row and row< rows and 0<=col and col < cols


rows = int(input())
collumns = rows
matrix =[[int(x) for x in input().split()] for _ in range (rows)]

line = input().split()

while line[0] != 'END':
    command = line[0]
    row,col = int(line[1]),int(line[2])
    value = int(line[-1])
    if is_valid(row,col,rows,collumns):
        if command == 'Add':
            matrix[row][col] += value

        elif command =='Subtract':
            matrix[row][col] -= value
    else:
        print(f'Invalid coordinates')
    line = input().split()


for row in matrix:
    print(*row,sep=' ')