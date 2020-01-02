from tkinter import *
import functions
from time import sleep

# window
window = Tk()
window.geometry('300x425')
window.resizable(0, 0)

# frames
f1 = Frame(window, width=300, height=425)
f1.place(x=0, y=0)
f2 = Frame(window, width=300, height=425)
f3 = Frame(window, width=300, height=425)
# buttons
b1 = Button(f1, text="Clock", command=lambda: functions.switch_frames(f1, f2))
b1.place(relx=0.25, rely=0.5, anchor='n')
b2 = Button(f1, text="Timer", command=lambda: functions.switch_frames(f1, f3))
b2.place(relx=0.75, rely=0.5, anchor='n')
b3 = Button(f2, text="Start", command=lambda: functions.time_start(window, c, l_s, l_m, l_h))
b3.place(x=0, y=0)
b4 = Button(f2, text="Stop", command=lambda: functions.time_stop())
b4.place(x=75, y=0)
#canvas
c = Canvas(f2, width=300, height=400)
c.place(x=0, y=50)
#lines
l_s = c.create_line(150, 200, 150, 100, fill='red')
l_m = c.create_line(150, 200, 150, 100, width=2)
l_h = c.create_line(150, 200, 150, 80, width=3)

# circle
oval = c.create_oval(50, 100, 250, 300)

def run_app():
    window.mainloop()

