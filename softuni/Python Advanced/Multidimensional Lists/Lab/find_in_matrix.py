rows = int(input())

matrix = []

for i in range(rows):
    matrix.append(list(input()))

found = False
ch = input()

for row in range(len(matrix)):
    for collumn in range(len(matrix[row])):
        if ch in matrix[row][collumn]:
            found = True
            break
    if found:
        break        
if found:
    print(f'({row}, {collumn})')

else:
    print(f'{ch} does not occur in the matrix')