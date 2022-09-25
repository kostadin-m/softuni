rows,col = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()]for _ in range(rows)]

final={
    'biggest': -2000,
    'row': 0,
    'col': 0
}

for i in range(rows -2):
    for x in range(col -2):
        sum_total = 0
        for check in range(i, i + 3):
            sum_total += sum(matrix[check][x: x + 3])
        if final["biggest"] < sum_total:
            final["biggest"] = sum_total
            final["row"] = i
            final["col"] = x


print(f"Sum = {final['biggest']}")

for roww in range(final["row"],final["row"]+ 3):
    col = final["col"] 
    print(" ".join([str(x) for x in matrix[roww][col: col+ 3]]))


