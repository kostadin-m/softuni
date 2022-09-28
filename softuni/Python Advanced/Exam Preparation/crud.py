size = 6
matrix = [[str(x) for x in input().split()]for _ in range(size)]
row, col = [int(x) for x in input().strip('()').split(', ')]
positions = {
    'up': [-1, 0], 'down': [1, 0], 'right': [0, 1], 'left': [0, -1]}

while True:
    commands = input().split(', ')
    if commands[0] == 'Stop':
        break
    command, position, = commands[0], commands[1]
    next_row, next_col = row + positions[position][0], col + positions[position][1]

    if 0 <= next_row <= size and 0 <= next_col <= size:
        row, col = next_row, next_col

        if command == 'Create':
            if matrix[row][col] == '.':
                matrix[row][col] = commands[2]
        elif command == 'Update':
            if matrix[row][col] != '.':
                matrix[row][col] = commands[2]
        elif command == 'Read':
            if matrix[row][col] != '.':
                print(matrix[row][col])
        elif command == 'Delete':
            if matrix[row][col] != '.':
                matrix[row][col] = '.'
for i in matrix:
    print(*i, sep=' ')
