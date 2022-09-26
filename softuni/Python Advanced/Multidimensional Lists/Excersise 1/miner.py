def valid_index(row,col):
    if command == 'up':
        return row-1,col
    if command == 'down':
        return row+1,col
    if command == 'right':
        return row,col +1
    if command == 'left':
        return row,col-1


def check_index():
    global coal_counter
    if matrix[miner_row][miner_col] =='*':
        pass
    elif matrix[miner_row][miner_col] == 'c':
       coal_counter -= 1 
       matrix[miner_row][miner_col] = '*'
    if coal_counter ==0:
        return True
    elif matrix[miner_row][miner_col] == 'e':
        return True


n = int(input())
commands = input().split()

coal_counter = 0
matrix = []
finished = False

for rows in range(n):
    row = [str(x) for x in input().split()]
    matrix.append(row)
    if 'c' in row:
        coal_counter += row.count('c')
    for coll in range(n):
        el = row[coll]
        if el == 's':
            miner_row = rows
            miner_col = coll

for command in commands:
    next_row, next_col = valid_index(miner_row,miner_col)
    if next_row< 0 or next_row >= n or next_col< 0 or next_col >= n:
        continue
    miner_row = next_row
    miner_col = next_col
    if check_index():
        finished = True
        break
if coal_counter == 0:
    print(f'You collected all coal! ({miner_row}, {miner_col})')
elif finished:
    print(f'Game over! ({miner_row}, {miner_col})')
else:
    print(f'{coal_counter} pieces of coal left. ({miner_row}, {miner_col})')