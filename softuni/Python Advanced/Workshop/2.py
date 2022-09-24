class Player:
    def __init__(self,name,sign):
        self.name = name
        self.sign = sign


def read_player():
    player_one = input('Player one name: ')
    player_two = input('Player two name: ')

    one = input(f'{player_one}, would you like to play with X or O:').upper()
    if one  in ['X','O']:
        two = 'O' if one == 'X' else 'X'
        return Player(player_one,one), Player(player_two,two)
    else:
        print('Wrong input')
        read_player()



def board_init_():
    size = 3
    result = []
    for _ in range(size):
        result.append([None] * size)
    return result


def check(mapper,pos):
    try:
        position = mapper[pos]
    except KeyError:
        print(f'Invalid position')
    board_row,board_col = position
    if board[board_row][board_col] == None :
        board[board_row][board_col] = current_player.sign
        show_board(board)
    else:
        print('Invalid position')



def show_board(board):
    for index in board:
        print('|  ',end='')
        print('  |  '.join([x if x is not None else ' ' for x in index]),end='')
        print('  |')



def check_winner(board):
    for row in board:
        if all([x == current_player.sign for x in row]):
            return True
    
    for column in range(len(board)):
        result = True 
        for row in range(len(board)):
            if board[row][column] != current_player.sign:
                result = False
        if result:
            return result
    
    left_diagonal = True
    right_diagonal = True
    for index in range(len(board)):
        if board[index][index] != current_player.sign:
            left_diagonal = False
        if board[index][len(board) -1 - index] != current_player.sign:
            right_diagonal = False
    return left_diagonal or right_diagonal




print(f'This is the numeration on the board:')
print(f'| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 | ')

board_mapper = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],}


board = board_init_()
first_player,second_player = read_player()
print(f'{first_player.name} starts first! ')


turn = 1

while True:
    current_player = first_player if turn % 2 != 0 else second_player
    position = int(input((f'{current_player.name} choose a free position [1-9]')))
    if 1 <= position <=9:
        check(board_mapper,position)
        if check_winner(board):
            print(f'{current_player.name} won!')
            quit()
    else:
        print('Invalid position! Try again')
        continue
    turn +=1