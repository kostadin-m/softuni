try:
    file = open('text.txt', 'rw')
    print(f'File found')
except:
    print(f'File not found')