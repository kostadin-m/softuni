rows = int(input())
even_matrix = []

for i in range(rows):
    row = [int(x) for x in input().split(', ')]
    even_matrix.append([int(x) for x in row if x % 2 ==0])
print(even_matrix)