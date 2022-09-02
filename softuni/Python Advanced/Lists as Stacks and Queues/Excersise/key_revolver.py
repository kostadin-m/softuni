from collections import deque


price_for_a_bullet = int(input())
size_of_a_gun_barrel = int(input())
bullets = input().split()
locks = deque(input().split())
value_of_the_inteligence = int(input())
barrel = size_of_a_gun_barrel


broken_locks = False

while len(bullets) != 0: 
    bullet_shot = bullets.pop()
    barrel -=1
    value_of_the_inteligence -= price_for_a_bullet
    
    if int(bullet_shot) <= int(lock_shot):
        print(f'Bang!')
        lock_shot = locks.popleft()
    
    else:
        print('Ping!')
    if barrel == 0:
        print(f'Reloading!')
        barrel = size_of_a_gun_barrel

if broken_locks:
    print(f'{len(bullets)} bullets left. Earned ${value_of_the_inteligence}$')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")





