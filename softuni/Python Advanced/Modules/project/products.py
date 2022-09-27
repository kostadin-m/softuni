import json
import tkinter as tk
from screen import clear_screen
import os


ADMINS = 'db/admins.txt'
CURRENT = 'db/session.txt'
PRODUCTS = 'db/products.txt'
USERS = 'db/users.txt'
image_folder = os.path.dirname(__file__)


def render_products(window, admin=False):
    clear_screen(window)
    row = 0
    col = 0
    max = 4
    with open(ADMINS) as admins, open(CURRENT) as current:
        current_user = current.readline()
        list_of_admins = admins.readlines()
        for line in list_of_admins:
            if current_user == line.strip():
                admin = True
    with open(PRODUCTS, 'r') as file:
        data = file.readlines()
        for line in data:
            product = json.loads(line.strip())
            print(product)
            if col == max:
                row = 0
                col = 0
                row += 4

            tk.Label(window, text=product['name'],).grid(row=row+1, column=col, pady=2)

            from PIL import ImageTk, Image

            image = Image.open(os.path.join(os.path.join(image_folder, "images"), product['img_path']))
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            img_label = tk.Label(image=photo)
            img_label.image = photo
            img_label.grid(row=row+2, column=col)

            tk.Label(window, text=product['count']).grid(row=row+3, column=col)

            button = tk.Button(window, text=f'Buy {product["id"]}', bg='green')
            button.configure(command=lambda b=button: buy_product(window, b))
            button.grid(row=row+4, column=col)
            col += 1
    if admin:
        admin_button = tk.Button(
            window,
            text='Add new products',
            bg='black',
            fg='white',
            command=lambda: add_product(window,admin_button,admin_label),
        )
        admin_button.place(x=430, y=20)

        admin_label = tk.Label(window, text='Welcome admin')
        admin_label.place(x=450, y=0)
    else:
        tk.Label(window, text='Welcome user').place(x=450, y=0)


def buy_product(window, button):
    _, product_id = button.cget("text").split()
    product_id = int(product_id)
    with open(CURRENT) as current, open(USERS, 'r+', newline='\n') as file:
        username = current.readline()
        data = file.readlines()
        file.seek(0)
        for line in data:
            user = json.loads(line.strip())
            if user['username'] == username:
                user['products'].append(product_id)
            file.write(json.dumps(user) + "\n")

    update_product_quantity(product_id)
    render_products(window)


def update_product_quantity(product_id):
    with open(PRODUCTS, 'r+') as file:
        data = file.readlines()
        file.seek(0)
        for line in data:
            current_products = json.loads(line.strip())
            if current_products['id'] == product_id:
                current_products['count'] -= 1
            file.write(json.dumps(current_products) + "\n")


def add_product(window, b, l):
    clear_screen(window)
    b.destroy()
    l.destroy()

    tk.Label(window, text='Product Name').grid(row=0,column=0)
    product_name = tk.Entry()
    product_name.grid(row=0, column=1)

    tk.Label(window, text='Product picture name').grid(row=1, column=0)
    picture_name = tk.Entry()
    picture_name.grid(row=1,column=1)

    tk.Label(window, text='Quantity').grid(row=2, column=0)
    quantity = tk.Entry()
    quantity.grid(row=2,column=1)

    tk.Button(
        window, text='Add',
        bg='black',
        fg='white',
        command=lambda: update_products(window, product_name.get(),
                                        picture_name.get(), quantity.get())).grid(row=3, column=0)


def update_products(window, name, pic_name, count):
    with open(PRODUCTS, 'r+', newline='\n') as products:
        product = products.readlines()
        product_obj= {
            'id': len(product) + 1,
            'name': name,
            'img_path': pic_name,
            'count': int(count)
        }
        products.write(json.dumps(product_obj))
    render_products(window)
