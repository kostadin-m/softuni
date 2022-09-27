from collections import deque

filled_boxes = 0
box_size = 50
eggs = deque([int(x) for x in input().split(', ')])
papers = [int(x) for x in input().split(', ')]

while eggs and papers:
    egg = eggs.popleft()
    paper = papers[-1]
    if egg <= 0:
        continue
    elif egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue
    total = egg + paper
    if total <= box_size:
        filled_boxes += 1
    papers.pop()

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if papers:
    print(f'Pieces of paper left: {", ".join(str(x) for x in papers)}')
if eggs:
    print(f'Eggs left: {", ".join(str(x) for x in eggs)}')
