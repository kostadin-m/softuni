size = int(input())
matrix = []
commands = {
    'up':[-1,0], 'down': [1,0],
    'right':[0,1], 'left':[0,-1]
}
def is_inside(row,col,size):
    return 0<=row < size and 0<= col < size

for i in range(size):
    matrix.append([str(x) for x in input().split()])
    for x in range(size):
        if matrix[i][x] == 'B':
            bunny_row,bunny_col = i,x

best_score = float('-inf')
best_path = []
best_direction =[]

for direction,move in commands.items():
    row,col = bunny_row,bunny_col
    current_score = 0
    path = []

    while True:
        row,col = row + move[0],col + move[1]
        if not is_inside(row,col,size):
            break

        if  matrix[row][col] == 'X':
            break
        path.append([row,col])
        current_score += int(matrix[row][col])
    if current_score > best_score and path:
        best_score = current_score
        best_path = path
        best_direction = direction


print(best_direction)
print('\n'.join([str(x) for x in best_path]))
print(best_score)
