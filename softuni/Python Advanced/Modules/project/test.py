with open('db/user_credentials.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        username, password = line.strip().split(', ')
        if 'kostadin' == username and password == '12345678':
            continue