try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

finally:
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.title('Gomoku')


    def button_clicked():

        print('Game start')
        # 此处为游戏入口


    button = ttk.Button(
        root,
        text='Start',
        command=button_clicked
    )
    button.pack(
        expand=True
    )
    window_width = 800
    window_height = 600

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.resizable(False, False)

    root.attributes('-topmost', 1)

    root.iconbitmap('./image/G.ico')

    root.mainloop()

# import tkinter as tk
# from tkinter import ttk
# def return_pressed(event):
#     print('Return key pressed.')
# root = tk.Tk()
# btn = ttk.Button(root, text='Save')
# btn.bind('<Down>', return_pressed)
# btn.focus()
# btn.pack(expand=True)
# root.mainloop()
# root.minsize(int(window_width/2), int(window_height/2))
# root.maxsize(window_width*2, window_height*2)
# root.attributes('-alpha', 1)
# message = ttk.Label(root)
# message.config(text='Gomoku')
# message.pack()
