from collections import deque
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f'{hour:02d}:{minutes:02d}:{seconds:02d}'
def to_seconds(timestr):
    
    seconds= 0
    for part in timestr.split(':'):
        seconds= seconds*60 + int(part, 10)
    return seconds

commands_for_robots = deque()
robots = input().split(';')
robots_work_time = {}
robot_busy_until = {}


for index in robots:
    robot, process_time = index.split('-')
    robots_work_time[robot] = int(process_time)
    robot_busy_until[robot]= -1
time = to_seconds(input())

while True:
    command = input()
    if command == 'End':
        break
    commands_for_robots.append(command)

while commands_for_robots:
    time +=1
    items = commands_for_robots.popleft()
    for name,busy_until in robot_busy_until.items():
        if time >= busy_until:
            print(f'{name} - {items} [{convert(time)}]')
            robot_busy_until[name] = time + robots_work_time[name]
            break
    else:
        commands_for_robots.append(items)

