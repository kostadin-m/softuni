line = input()
index_stack = []


for i in range(len(line)):
    if line[i] == '(':
        index_stack.append(i)
    elif line[i] == ')':
        start_index = index_stack.pop()
        print(f'{line[start_index:i+ 1]}')