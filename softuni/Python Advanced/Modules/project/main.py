import tkinter as tk
from screen import render_main_screen

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('600x800')
    window.title('My GUI Shop')
    render_main_screen(window)
    window.mainloop()



