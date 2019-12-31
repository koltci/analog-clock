from tkinter import *
import functions
from time import sleep

# window
window = Tk()
window.geometry('300x425')
window.resizable(0, 0)

b1 = Button(window, text="Start", command=lambda: functions.time_start(window, c, l_s, l_m, l_h))
b1.place(x = 0, y = 0)
b2 = Button(window, text="Stop", command=lambda: functions.time_stop())
b2.place(x = 75, y = 0)

#canvas
c = Canvas(window, width=300, height=400)
c.place(x = 0, y = 50)
#lines
l_s = c.create_line(150, 200, 150, 100, fill='red')
l_m = c.create_line(150, 200, 150, 100, width=2)
l_h = c.create_line(150, 200, 150, 80, width=3)

# circle
oval = c.create_oval(50, 100, 250, 300)

def run_app():
    # window.update_idletasks()
    # window.update()
    mainloop()

