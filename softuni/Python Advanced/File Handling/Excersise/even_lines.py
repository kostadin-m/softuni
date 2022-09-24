chars = '-,,.!?'
with open('text.txt') as file:
    
    for row, line in enumerate(file):
        if row % 2 != 0:
            continue
        word = ' '.join(line.strip().split()[::-1])
        
        for char in chars:
            word = word.replace(char,'@')
        print(word)

 
