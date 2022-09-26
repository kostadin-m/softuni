def print_triangle(line):
    for row in range(1, line+1):
        for row1 in range(1,row+1):

            print(row1,end='')
        print()
    for row in range(line,0,-1):
        for row1 in range(row+1,0,-1):
            print(row,end='')
        print()