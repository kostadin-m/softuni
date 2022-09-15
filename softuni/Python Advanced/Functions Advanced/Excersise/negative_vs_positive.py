line = [int(x) for x in input().split()]

positive = sum([int(x) for x in line if x > 0])
negative = abs(sum([int(x) for x in line if x < 0]))


print(f'-{negative}')
print(positive)

if positive > negative:
    print(f'The positives are stronger than the negatives')
else:
    print(f'The negatives are stronger than the positives')