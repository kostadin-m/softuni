elements_count = int(input())

elements = set()
for _ in range(elements_count):
    how_many_elements = input().split()
    for element in how_many_elements:
        elements.add(element)

print("\n".join(elements))