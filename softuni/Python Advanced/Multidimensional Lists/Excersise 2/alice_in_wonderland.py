def find_alice():
    for row in range(size):
        if 'A' in matrix[row]:
            return row, matrix[row].index("A")

size = int(input())
matrix = [[str(x) for x in input().split()]for _ in range(size)]
collected_tea = 0
won = False
movement ={
    'up':[-1,0],
    'down':[1,0],
    'right':[0,1],
    'left':[0,-1]
}

alice_row,alice_col = find_alice()
matrix[alice_row][alice_col] ='*'

while True:
    command = input()
    next_row,next_col = alice_row + movement[command][0], alice_col + movement[command][1]
    if 0 > next_row or next_row >= size or 0> next_col or next_col >= size:
        break
    if matrix[next_row][next_col] =='R':
        matrix[next_row][next_col] = '*'
        break
    if matrix[next_row][next_col].isdigit():
        collected_tea += int(matrix[next_row][next_col])
    matrix[next_row][next_col] ='*'
    if collected_tea >= 10:
        won = True
        break
    alice_row,alice_col = next_row,next_col

if won:
    print(f"She did it! She went to the party.")
else:
    print(f"Alice didn't make it to the tea party.")
for row in matrix:
    print(*row,sep =' ')