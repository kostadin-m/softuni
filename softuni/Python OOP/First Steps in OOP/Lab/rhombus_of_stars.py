number = int(input())


def print_rhombus(n):
    for row in range(1, n + 1):  # Upper part
        print_row(row, n)
    for row in range(n - 1, 0, -1):  # Bottom part
        print_row(row, n)


def print_row(num, n):  # Prints whitespaces and '*'
    for spaces in range(n - num):
        print(' ', end='')
    for stars in range(1, num):
        print('*', end=' ')
    print('*')


print_rhombus(number)

