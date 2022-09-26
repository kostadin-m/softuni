def clear_screen(window):
    for el in window.grid_slaves():
        el.destroy()
