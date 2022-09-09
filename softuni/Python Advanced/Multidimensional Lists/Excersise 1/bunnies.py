rows,collumns = [int(x) for x in input().split()]
matrix =[[str(x) for x in list(input())]for _ in range(rows)]
commands = list(input())


bunnies,new_bunnies =set(),set()
won,dead = False,False
movement = {
    'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1],
    }

def is_escaped(row,col,rows,cols):
    return  row < 0 or row>= rows or col < 0 or col >= cols


def find_player_bunny():
    for row in range(rows):
        for col in range(collumns):
            if matrix[row][col] == 'P':
                return f'{row} {col}'
            if matrix[row][col] == 'B':
                bunnies.add(f'{row} {col}')


def bunny_spread(bunnies,new_bunnies):
    for bunny in bunnies:
        bunny_row,bunny_col = [int(x) for x in bunny.split()]
        for i in range(bunny_row-1,bunny_row+2):
            if not is_escaped(i,bunny_col,rows,collumns):
                new_bunnies.add(f'{i} {bunny_col}')
                matrix[i][bunny_col] = 'B'
        for x in range(bunny_col-1,bunny_col+2):
            if not is_escaped(bunny_row,x,rows,collumns):
                new_bunnies.add(f'{bunny_row} {x}')
                matrix[bunny_row][x] = 'B'
    return bunnies.union(new_bunnies)

player_row,player_col = [int(x) for x in find_player_bunny().split()]
matrix[player_row][player_col] ='.'
find_player_bunny()



for command in commands:
    next_row,next_col = player_row + movement[command][0],player_col + movement[command][1]
    if is_escaped(next_row,next_col,rows,collumns):
        won = True
    elif matrix[next_row][next_col] =='B':
        dead = True
        player_row,player_col = next_row,next_col
    else:
        player_row,player_col = next_row,next_col
    bunnies =bunny_spread(bunnies,new_bunnies)
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