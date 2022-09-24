try:
    with open('numbers.txt') as file:   
        print (sum([int(x) for x in open(file.readlines())]))
except:
    print('File not found')