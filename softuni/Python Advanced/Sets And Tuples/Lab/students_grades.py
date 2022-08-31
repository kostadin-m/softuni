from statistics import mean

n = int(input())
dict_name_grade = {}

for i in range(n):
    name, grades = input().split()
    grade = float(grades)
    if name in dict_name_grade:
        dict_name_grade[name].append(grade)
    else:
        dict_name_grade[name] = [grade]
    
for data in dict_name_grade.items():
    print(f"{data[0]} -> {' '.join([f'{x:.2f}' for x in data[1]])} (avg: {(sum(data[1]) / len(data[1])):.2f})")