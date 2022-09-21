problems = {
    ValueError: 'Please enter an integer!',
    ZeroDivisionError: 'Second number cannot be divided by zero'
}

while True:
    try:
        x = int(input())
        y = int(input())
        print(x/y)
        break
    except (ValueError,ZeroDivisionError) as problems:
        print(problems)
