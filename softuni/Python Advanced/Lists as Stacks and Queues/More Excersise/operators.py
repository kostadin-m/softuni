from collections import deque
op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '/': lambda x, y: x//y,
      '*': lambda x, y: x * y,}

line = input().split()
stacked  = deque()
for ch in line:
    if ch in '-+*/':
        while len(stacked) > 1:
                first = int(stacked.popleft())
                second = int(stacked.popleft())
                result = op[ch](first,second)
            
                stacked.appendleft(result)
    else:   
        stacked.append(ch)

print(*stacked)