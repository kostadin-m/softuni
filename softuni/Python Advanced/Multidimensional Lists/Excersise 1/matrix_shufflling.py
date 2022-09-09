def valid_input(row,col,rows,cols):
    return row < 0 or col < 0 or col > cols or row > rows


rows,collumns = [int(x) for x  in input().split()]

matrix=[]

for i in range(rows):
    matrix.append(input().split())


while True:
    command = input().split()
    if command[0] =='END':
        break
    if len(command) != 5 or command[0] != 'swap':
        print('Invalid input!')
        continue
    row1,col1,row2,col2 = [int(x) for x in command[1:]]

    if valid_input(row1,col1,rows,collumns) or valid_input(row2,col2,rows,collumns):
        print('Invalid input!')
        continue
    matrix[row1][col1],matrix[row2][col2] = matrix[row2][col2],matrix[row1][col1]
    for row in matrix:
        print(*row,sep=' ')