from fibonaci.functions import *

while True:
    commands = input().split()
    if commands[0] == 'Stop':
        break
    command = commands[0]
    line = int(commands[-1])

    if command == 'Create':
        fibo = create(line)
        print(*fibo, sep=' ')
    elif command == 'Locate':
        try:
            print(locate(line, fibo))
        except NameError:
            print(f'Cannot locate in empty sentence')
