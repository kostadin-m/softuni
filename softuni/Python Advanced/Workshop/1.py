class FullCollumnError(Exception):
    pass

def check_valid(col,played):
    return  played < col and  played >= 0


def check(matrix,rows,colls,index,player):
    while not check_valid(colls,player):
        player = int(input(f'Player {index}, This collumn is not valid please sellect a collumn in range 1 - {colls}: '))  -1 
    for i in range(rows-1,-1,-1):
        if matrix[i][player] == 0:
            matrix[i][player] = index
            return i,player
    raise FullCollumnError


def is_player_num(matrix,row,col,player):
    if 0> col or 0 > row:
        return False
    try:
        if matrix[row][col] == player:
            return True
    except IndexError:
        return False       
    return False


def winner(matrix,rows,cols,player,slots=4):
    
    def check_horizontal():
        is_right = [is_player_num(matrix,rows,cols+i,player)for i in range(slots)].count(True)
        is_left =  [is_player_num(matrix,rows,cols-i,player)for i in range(slots)].count(True)
        return int(is_right + is_left) > slots
    
    
    def check_vertical():
        is_up = [is_player_num(matrix,rows-i,cols,player)for i in range(slots)].count(True)
        is_down = [is_player_num(matrix,rows+i,cols,player) for i in range(slots)].count(True)
        return int(is_up +is_down) > slots
    
    
    def check_diagonal():
        is_up_right = [is_player_num(matrix,rows-i,cols+i,player) for i in range(slots)].count(True)
        is_down_left = [is_player_num(matrix,rows+i,cols-i,player) for i in range(slots)].count(True)
        return int(is_up_right + is_down_left) > slots

    
    if any([check_horizontal(),check_vertical(),check_diagonal()]):
        return True
    return False


def script():
    players_count = int(input('Count of players: '))
    rows,colls = 6,7
    matrix = [[0 for _ in range(colls)]for _ in range(rows)]
    while True:
        
        for player_number in range(1,players_count+1):
            picked_col = int(input(f'Player {player_number}, please choose a collumn: ')) -1
            try:
                last_row,last_col = check(matrix,rows,colls,player_number,picked_col)
            except FullCollumnError:
                
                picked_col = int(input((f'Player {player_number}, please choose another collumn, this one is full: ')))
                continue
            
            if winner(matrix,last_row,last_col,player_number): # If we won we check if the player wants to restart the program
                print(f'The winner is player {player_number}')
                reset = input('Restart? (y/n): ')
                if reset =='y':
                    script()
                else:
                    quit()
            print(*matrix,sep= '\n')

script()