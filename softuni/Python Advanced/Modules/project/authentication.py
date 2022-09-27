import tkinter as tk
import json
from products import render_products
from screen import clear_screen

USERS = 'db/users.txt'
CREDENTIALS = 'db/user_credentials.txt'
CURRENT_SESSION = 'db/session.txt'


def render_main_screen(window, is_register=False,correct_name_pwrod=False):
    clear_screen(window)

    tk.Label(window, text='Username').grid(row=0)
    username = tk.Entry()
    username.grid(row=0, column=1)

    tk.Label(window, text='Password').grid(row=1)
    password = tk.Entry(window, show='*')
    password.grid(row=1, column=1)

    tk.Button(window,
              text='Enter',
              bg='green',
              command=lambda: check_login_info(window, username.get(), password.get())
              ).grid(row=2, column=0)

    if is_register:
        tk.Label(window, text="Thanks for creating account").grid(row=0, column=2)
    else:
        tk.Label(window, text="Don't have an account yet?").grid(row=0, column=2)
        tk.Button(
            window,
            text='Register',
            bg='black',
            fg='white',
            command=lambda: render_register_screen(window)
        ).grid(row=1, column=2)


def render_register_screen(window):
    clear_screen(window)
    tk.Label(window, text='Username', ).grid(row=0)

    username = tk.Entry()
    username.grid(row=0, column=1)

    tk.Label(window, text='Password').grid(row=1)
    password = tk.Entry(window, show='*')
    password.grid(row=1, column=1)

    tk.Label(window, text='First Name').grid(row=2)
    first_name = tk.Entry()
    first_name.grid(row=2, column=1)

    tk.Label(window, text='Last Name').grid(row=3)
    last_name = tk.Entry()
    last_name.grid(row=3, column=1)

    tk.Button(window, text='Register',
              bg='black',
              fg='white',
              command=lambda: register(window, username.get(), password.get(),
                                       first_name.get(), last_name.get())).grid(row=5)


def register(window, username, pword, first, last, taken_name=False):
    with open(USERS) as file:
        for user_line in file:
            user = json.loads(user_line.strip())
            if user['username'] == username:
                taken_name = True

    if len(username) < 8:
        tk.Label(window, text='Name is too short').grid(row=0, column=2)
    elif taken_name:
        tk.Label(window, text='Username already exists').grid(row=0, column=2)
    else:
        user_info = {
            'username': username,
            'password': pword,
            'first_name': first,
            'last_name': last
        }
        user_info.update({"products": []})
        with open(USERS, 'a', newline='') as file:
            file.write(json.dumps(user_info))
            file.write('\n')
        with open(CREDENTIALS, 'a', newline='') as file:
            file.write(f"{username}, {pword}\n")
        render_main_screen(window, is_register=True)


def check_login_info(window, user, pword):
    with open(CREDENTIALS, 'r') as file:
        data = file.readlines()
        for line in data:
            username, password = line.strip().split(', ')
            if user == username and password == pword:
                with open(CURRENT_SESSION, 'w') as session:
                    session.write(user)
                render_products(window)
            else:
                tk.Label(window, text="Wrong password").grid(row=2, column=1)

