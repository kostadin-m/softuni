clothing = [int(x) for x in input().split()]
capacity = int(input())

rack = 1
current_rack = capacity

while clothing:
    clothes = clothing[-1]

    if current_rack >= clothes:
        current_rack -=clothes
        clothing.pop()
    else:
        current_rack = capacity
        rack +=1

print(rack)

