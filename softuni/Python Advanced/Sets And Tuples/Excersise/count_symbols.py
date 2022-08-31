line = str(input())
count_of_characters = {}

for ch in line:
    if ch not in count_of_characters.keys():
        count_of_characters[ch] = 0
    count_of_characters[ch] +=1

for pair in sorted(count_of_characters.items()):
    print(f'{pair[0]}: {pair[1]} time/s')