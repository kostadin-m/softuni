def is_valid(row,col,rows,cols):
    return 0<= row and row< rows and 0<= col and col < cols

def check_movement():
    knight = 0
    for movement_row,movement_col in movement.values():
        next_row,next_col = knight_row + movement_row , knight_col + movement_col
        if is_valid(next_row,next_col,rows,collumns) and matrix[next_row][next_col] =='K':
            knight +=1
    return knight

rows= int(input())
collumns = rows
knight_position = set()
matrix = []
removed = 0
movement = {
    "up left": [-2, -1], "up right": [-2, 1], "down left": [2, -1], "down right": [2, 1],
    "left up": [-1, -2], "left down": [1, -2], "right up": [-1, 2], "right down": [1, 2],
}
for row in range(rows):
    matrix.append([str(x) for x in list(input())])
    for col in range(collumns):
        if matrix[row][col] == 'K':
            knight_position.add(f'{row} {col}')

while True:
    value = {}
    for row in range(rows):
        for col in range(collumns):
            if matrix[row][col] == '0':
                continue
            knight_row,knight_col = row,col
            interfered_knights = check_movement()
            if interfered_knights:
                value[knight_row, knight_col] = interfered_knights
    if not value:
        break
    
    
    best_counter,row,col= 0,0,0
    for coords,counter in value.items():
        if counter > best_counter:
            best_counter = counter
            row = coords[0]
            col = coords[-1]
    
    matrix[row][col] = '0'
    knight_position.remove(f'{row} {col}')
    removed +=1
print(removed)