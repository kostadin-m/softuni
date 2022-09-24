import re

with open('text.txt') as file:
    searched = file.read()

words_count = {}

with open('words.txt') as file:
    words = file.read()
    for word in words.split():
        pattern = fr'\b{word}\b'
        counter = len(re.findall(pattern,searched,re.IGNORECASE))
        words_count[word] = counter

with open('output.txt','w') as file:
    sorted_words = sorted(words_count.items(), key= lambda kvpt: -kvpt[1])
    for key,value in sorted_words:
        file.write(f'{key} - {value}\n')