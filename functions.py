from math import sin
from math import cos
import math
from tkinter import *
from time import sleep
import time
# import sched, time
import threading
import GUI

act = False
alpha = 0


def lines_move(tk, canvas1, line1, line2, line3):
    global alpha
    x2 = 100 * sin(math.radians(alpha))
    y2 = 100 * cos(math.radians(alpha))
    x4 = 100 * sin(math.radians(alpha / 60))
    y4 = 100 * cos(math.radians(alpha / 60))
    x6 = 80 * sin(math.radians(alpha / 3600))
    y6 = 80 * cos(math.radians(alpha / 3600))
    canvas1.coords(line1, 150, 200, (150 + x2), (200 - y2))
    canvas1.coords(line2, 150, 200, (150 + x4), (200 - y4))
    canvas1.coords(line3, 150, 200, (150 + x6), (200 - y6))
    tk.update_idletasks()
    tk.update()
    alpha = alpha + 6
    # print(str(alpha) + ", " + str(150 - x2) + ", " + str(200 - y2))
    sleep(1)


def time_start(tkint, canv, l1, l2, l3):
    global act
    act = True
    while act == True:
        t1 = threading.Thread(target=lines_move(tkint, canv, l1, l2, l3))
        # t2 = threading.Thread(target=GUI.run_app())
        t1.start()
        # t2.start()


def time_stop():
    global act
    act = False


def switch_frames(frame1, frame2):
    frame1.place_forget()
    frame2.place(x=0, y=0)

