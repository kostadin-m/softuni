def math_operation(operation):
    op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '/': lambda x, y: x // y,
          '*': lambda x, y: x * y}

    num1, operator, num2 = operation
    print(f'{op[operator](int(num1), int(num2)):.2f}')