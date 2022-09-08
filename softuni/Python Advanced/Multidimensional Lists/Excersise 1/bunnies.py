def check_if_escaped(row,col,rows,collumns):
    return row < 0 or row >= rows or col < 0 or col >= collumns
def next_pos(row,col,com):
    if com =='U':
        return row - 1,col
    elif com=='D':
        return row + 1,col
    elif com =='R':
        return row,col + 1
    elif com =='L':
        return row,col -1
rows,collumns = [int(x) for x in input().split()]
matrix = []
bunnies = set()
for i in range(rows):
    row = [str(x) for x in list(input())]
    matrix.append(row)
    for x in range(collumns):
        col = row[x]
        if col =='P':
            player_row = i
            player_col = x
        elif col =='B':
            bunnies.add(f'{i} {x}')
commands = list(input())
won = False
dead = False
new_bunnies = set()
matrix[player_row][player_col] ='.'
for command in commands:
    next_row,next_col = next_pos(player_row,player_col,command)
    if check_if_escaped(next_row,next_col,rows,collumns):
        won = True
    elif matrix[next_row][next_col] == 'B':
        dead = True
        player_row,player_col = next_row,next_col
    else:
        player_row,player_col = next_row,next_col
    
    for bunny in bunnies:   
        bunny_row, bunny_col = [int(x) for x in bunny.split()]
        
        for i in range(bunny_row-1,bunny_row+2):
            if not check_if_escaped(i,bunny_col,rows,collumns):
                
                new_bunnies.add(f'{i} {bunny_col}')
                matrix[i][bunny_col] = 'B'
        
        for x in range(bunny_col-1,bunny_col+2):
            if not check_if_escaped(bunny_row,x,rows,collumns):
                
                new_bunnies.add(f'{bunny_row} {x}')
                matrix[bunny_row][x] = 'B'
    
    bunnies = bunnies.union(new_bunnies)
    
    if matrix[player_row][player_col] =='B':
        dead = True
    
    if won or dead:
        break

for row in matrix:
    print(*row,sep ='')
if won:
    print(f'won: {player_row} {player_col}')
elif dead:
    print(f'dead: {player_row} {player_col}')