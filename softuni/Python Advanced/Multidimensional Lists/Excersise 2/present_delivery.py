presents = int(input())
matrix = [[str(x) for x in input().split()] for _ in range(int(input()))]
count_nice_kids = [sum([matrix[row].count("V") for row in range(len(matrix))])]
happy = False
final_nice_kids = count_nice_kids[0]


movement ={
    'up':[-1,0], 'down':[1,0],
    'right':[0,1], 'left':[0,-1]
}

def is_inside(row,col,size):
    return 0 <= row < size and 0 <= col < size



def find_santa():
    for row in range(len(matrix)):
        if 'S' in matrix[row]:
            col = matrix[row].index("S")
            matrix[row][col] = "-"
            return row, col


def check(row,col):
    global happy,presents
    if is_inside(row,col,len(matrix)):
        if matrix[row][col] =='V':
            presents -= 1
            count_nice_kids[0] -= 1
        elif matrix[row][col] =='C':
            happy = True
        elif matrix[row][col] =='X' and happy:
            presents -=1
    matrix[row][col]='-'
    return row,col



def happy_santa():
    global santa_row,santa_col
    for pair in movement.items():
            next_row,next_col = santa_row + pair[1][0],santa_col + pair[1][1]
            check(next_row,next_col)




santa_row,santa_col = find_santa()

while True:
    command = input()
    if command =='Christmas morning':
        break
    next_row,next_col = santa_row + movement[command][0],santa_col + movement[command][1]
    santa_row,santa_col = check(next_row,next_col)
    
    if happy:
        happy_santa()
    
    if not presents:
        break


matrix[santa_row][santa_col] ='S'

if presents ==0 and count_nice_kids[0] >0:
    print(f'Santa ran out of presents!')
for row in matrix:
    print(*row,sep=' ')
if count_nice_kids[0] ==0:
    print(f'Good job, Santa! {final_nice_kids} happy nice kid/s.')
else:
    print(f"No presents for {count_nice_kids[0]} nice kid/s.")
