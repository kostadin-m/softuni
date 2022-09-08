def check(row,col,size):
    if 0 <= row < size and 0 <= col < size and matrix[row][col] > 0:
        matrix[row][col] -= bomb_size
            

matrix = [[int(x) for x in input().split()]for _ in range(int(input()))]
rows = len(matrix)
collumns = rows
bombs = input().split()

for bomb in bombs:
    bomb_row,bomb_col = [int(x) for x in bomb.split(',')]
    if matrix[bomb_row][bomb_col] > 0:
        bomb_size = matrix[bomb_row][bomb_col]
    
        for row in range (bomb_row -1,bomb_row +2):
            for col in range(bomb_col -1 , bomb_col+2):
                check(row,col,rows)
alive = []

for i in range(rows):
    for x in range(collumns):
        if matrix[i][x] > 0:
            alive.append(matrix[i][x])

print(f'Alive cells: {len(alive)}')
print(f'Sum: {sum(alive)}')

for row in matrix:
    print(*row,sep=' ')