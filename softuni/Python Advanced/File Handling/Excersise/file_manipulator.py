import os


def create(name):
    with open(name,'w+') as file:
        return file.write('')


def add_file(name):
    line = command[2]
    with open(name,'w+') as file:
        return file.write(line + '\n') 


def replace(name):
    old, new = command[2::]
    if os.path.exists(name):
        with open(name, 'r+') as file:
            new_content = file.read().replace(old,new)
            file.seek(0), file.truncate(0) # Removes old content
            
            return file.write(new_content) # Returns new content
    print('An error occurred')


def delete_file(name):
    if os.path.exists(name):
        return os.remove(name)
    print("An error occurred")


commands = {              # Key ; Input, Value ; Reference to a function
    'Create': create,
    'Add': add_file,
    'Replace': replace,
    'Delete': delete_file
}


while True:
    command = input().split('-')
    if command[0] == 'End':
        break
    try:
        commands[command[0]](command[1])
    except KeyError:
        print(f'An error occured')