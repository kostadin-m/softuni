op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '/': lambda x, y: x//y,
      '*': lambda x, y: x * y
}
num1, operator, num2 = input().split()

print(f'{op[operator](int(num1), int(num2)):.2f}')
