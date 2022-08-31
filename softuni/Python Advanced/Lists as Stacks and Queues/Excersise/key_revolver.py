from collections import deque


price_for_a_bullet = int(input())
size_of_a_gun_barrel = int(input())
bullets = input().split()
locks = deque(input().split())
value_of_the_inteligence = int(input())
barrel = size_of_a_gun_barrel


broken_locks = False

while len(bullets) != 0: 
    if barrel == 0:
        print(f'Reloading!')
        barrel = size_of_a_gun_barrel
    bullet_shot = bullets.pop()
    lock_shot = locks.popleft()
    if int(bullet_shot) > int(lock_shot):
        print('Ping!')
        barrel -=1
        locks.appendleft(lock_shot)
        value_of_the_inteligence -= price_for_a_bullet
    elif int(bullet_shot) <= int(lock_shot):
        print(f'Bang!')
        barrel -=1
        value_of_the_inteligence -= price_for_a_bullet
    if len(locks) <= 0:
        broken_locks = True
        break

if broken_locks:
    print(f'{len(bullets)} bullets left. Earned ${value_of_the_inteligence}$')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")




