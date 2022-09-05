from collections import deque


n = int(input())
stacked_numbers = []

def one():
    stacked_numbers.append(int(text))
def two():
    if stacked_numbers:
        stacked_numbers.pop()
def three():
    if stacked_numbers:
        print(max(stacked_numbers))
def four():
    if stacked_numbers:
        print(min(stacked_numbers))

commands = {
    1 : one,
    2 : two,
    3 : three,
}
for _ in range(n):
    line = deque(input().split())
    command = int(line.popleft())
    text = int(line[0]) if line else ''
    action = commands.get(command, four)
    action()


print(', '.join(str(x) for x in reversed(stacked_numbers)))

