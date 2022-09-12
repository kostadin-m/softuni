matrix =[[str(x) for x in input().split()] for _ in range(5)]
target_counter = [sum([matrix[row].count("x") for row in range(5)])]

movement ={
    'up':[-1,0], 'down':[1,0],
    'right':[0,1], 'left':[0,-1]
}

shot_targets = []
hit_targets = target_counter[0]



def find_position():
    for row in range(5):
        if "A" in matrix[row]:
            col = matrix[row].index("A")
            matrix[row][col] = "."
            return row, col


def is_inside(row,col):
    return 0 <= row < 5 and 0 <= col < 5



def shoot():
    global shot_targets,hit_targets
    bullet_row,bullet_col = player_row,player_col
    while True:
        next_row,next_col = bullet_row + movement[direction][0],bullet_col +movement[direction][1]
        if is_inside(next_row,next_col):
            if matrix[next_row][next_col] =='x':
                matrix[next_row][next_col] ='.'
                hit_targets -=1
                shot_targets.append([next_row, next_col])
                break
            bullet_row,bullet_col = next_row,next_col
        else:
            break
    return shot_targets,hit_targets


def move(row,col,direction, steps):
    total_step = [x * steps if x != 0 else 0 for x in movement[direction]]
    next_row,next_col = row + total_step[0], col + total_step[1]
    if is_inside(next_row,next_col) and matrix[next_row][next_col] == '.':
        matrix[row][col] =='.'
        matrix[next_row][next_col] ='A'
        return next_row,next_col
    return row,col
    


player_row,player_col = find_position()

for i in range(int(input())):
    command = input().split()
    direction = command[1]
    if command[0] =='move':
        player_row, player_col = move(player_row, player_col, command[1], int(command[-1]))
    elif command[0] =='shoot':
        shoot()
    if hit_targets == 0:
        break

if hit_targets ==0:
    print(f'Training completed! All {target_counter[0]} targets hit.')
else:
    print(f'Training not completed! {hit_targets} targets left.')
for i in shot_targets:
    print(i)