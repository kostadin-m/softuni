rows, collumns = [int(x) for x in input().split(', ')]
sums = 0
matrix = [[int(x) for x in input().split(', ')] for row in range(rows)]


max_sum  = {
    'max': -200,
    'row': 0,
    'col': 0
}

for row in range(rows-1):
    for collumn in range(collumns-1):
        sums = matrix[row][collumn]+\
        matrix[row][collumn+1]+\
        matrix[row+1][collumn]+\
        matrix[row +1 ][collumn+ 1]
        if max_sum['max'] < sums:
            max_sum['max'] = sums
            max_sum['row'] = row
            max_sum['col'] = collumn


for row in range(max_sum["row"], max_sum["row"] + 2):
    col = max_sum['col']
    print(" ".join([str(x) for x in matrix[row][col: col + 2]]))
print(max_sum['max'])
