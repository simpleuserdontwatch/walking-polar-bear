from tkinter import *
from tkinter.messagebox import *
from random import random
import pyautogui
from PIL import ImageTk, Image
def animate():
    global frame_index
    frame_index += 1
    if frame_index >= len(frames):
        frame_index = 0
    img = frames[frame_index]
    label.config(image=img)
    root.after(70, animate)
def gorandom(event):
    root.geometry(f'+{round(random()*w)-150}+{round(random()*h)-200}')
def onclose():
    if askyesno('Close?', 'Do you wish to close your very cool friend? :('):
        root.destroy()
w,h = pyautogui.size()
root = Tk()
root.protocol("WM_DELETE_WINDOW", onclose)
root.attributes('-topmost', True)
root.wm_attributes("-toolwindow", True)
root.title('friend!')
root.config(bg='white')
frame_index = 0
frames = []
gif_path = "polarbear.gif"
gif = Image.open(gif_path)
try:
    while True:
        frame = ImageTk.PhotoImage(gif.copy().resize((150,150)))
        frames.append(frame)
        gif.seek(len(frames))
except EOFError:
    pass
img = frames[0]
label = Label(root, image=img, borderwidth=0, cursor="hand1")
label.bind('<Button-1>',gorandom)
label.pack()
animate()
root.mainloop()
