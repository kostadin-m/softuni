with open('db/admins.txt') as admins, open('db/session.txt') as current:
    current_user = current.readline()
    list_of_admins = admins.readlines()
    for line in list_of_admins:
        if current_user == line.strip():
            admin = True