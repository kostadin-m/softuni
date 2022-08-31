from collections import deque

number_of_guest = int(input())
guest_list = set()

for guests in range (number_of_guest):
    line = input()
    guest_list.add(line)

command = input()

while command != 'END':
    guest_list.remove(command)
    command = input()

print(len(guest_list))
print('\n'.join(sorted(guest_list)))


