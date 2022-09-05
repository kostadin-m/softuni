
import time
from collections import deque


def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = 'CHECKING RESULTS... {:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def check_winner():
    global result
    winner = False
    for row in range(3):
        if game[row][0] == game[row][1] == game[row][2]: # Checking rows to see if 1/0 is a winner
            winner = True
            break
    for column in range(3): # If there is no winner in rows we check collumns
        if winner:
            break
        else:
            if game[0][column] == game[1][column] == game[2][column]:
                winner = True
    
    if not winner: #If there is no winner in collumns nor rows we check diagonals
        if game[0][0] == game[1][1] == game[2][2] or game[0][2] == game[1][1] == game[2][0]:
            winner = True
    result = game[0][0]
    return winner


table = deque([
    [0,0,0],
    [0,0,0],
    [0,0,0],
])
print(f'                         GAME BOARD          ')
print(' ')
for i in table:
    print('                          ',' '.join(str(x) for x in i[::-1]))

game = []

for x in range(3):
    current_row = list(input().split(' '))
    game.append(current_row)
    table.pop()
    table.appendleft(current_row)
print('                         FINAL BOARD                     ')
for i in table:
    print('                          ',' '.join(str(x) for x in i))

check_winner()

countdown(3)


if check_winner:
    print('                       WINNER: ',result.upper())
else:
    print('                        DRAW          ')