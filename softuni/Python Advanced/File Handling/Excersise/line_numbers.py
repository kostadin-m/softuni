import re

punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

with open('text.txt') as file, open('output.txt','w') as output:
    for row, line in enumerate(file):
        words = line.strip()      
        
        counter_for_words = len(re.findall(r'[a-zA-Z]' ,words))
        counter_for_signs = len([x for x in words if x in punctuation])
        
        output.write(f'Line {row}: {words} ({counter_for_words})({counter_for_signs})\n')