#
# import tkinter as tk
#
# try:
#     from ctypes import windll
#     windll.shcore.SetProcessDpiAwareness(1)
#
# finally:
#
#     root = tk.Tk()
#     root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window Demo')

window_width = 300
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)
# root.minsize(int(window_width/2), int(window_height/2))
# root.maxsize(window_width*2, window_height*2)

root.attributes('-alpha', 0.5)

root.attributes('-topmost', 1)

root.iconbitmap('')

root.mainloop()
