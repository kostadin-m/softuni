from collections import deque


price_for_a_bullet = int(input())
size_of_a_gun_barrel = int(input())
bullets = input().split()
locks = deque(input().split())
value_of_the_inteligence = int(input())
barrel = size_of_a_gun_barrel

while bullets and locks:
    
    bullet_shot = bullets.pop()
    lock_shot = locks[0]
    barrel -=1
    value_of_the_inteligence -= price_for_a_bullet
 
    if int(bullet_shot) <= int(lock_shot):
        print(f'Bang!')
        lock_shot = locks.popleft()
    
    else:
        print('Ping!')
    if bullets:
        if barrel == 0:
            print(f'Reloading!')
            barrel = size_of_a_gun_barrel
    else:
        continue


if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
     print(f'{len(bullets)} bullets left. Earned ${value_of_the_inteligence}')




