from curses import window
import math
from position_planetes import get_by_VSOP87 as pos
import temps
import time
import tkinter as tk

size = 600

def get_coords(L, B, R) :
    return [int((200 * R * math.sin(L)) -10 +size/2), int((200 * R * math.cos(L)) -10 +size/2), int((200 * R * math.sin(L)) +10+size/2), int((200 * R * math.cos(L)) +10 +size/2)]

def get_new(old, new) :
    return [new[0]-old[0], new[1]-old[1]]

window = tk.Tk()
canvas = tk.Canvas(window, width=size, height=size)
canvas.pack()

start_date = (2022, 1, 1)
mercure_pos = get_coords(*pos('Mercure', *start_date))
venus_pos = get_coords(*pos('Venus', *start_date))
terre_pos = get_coords(*pos('Terre', *start_date))
mars_pos = get_coords(*pos('Mars', *start_date))

mercure = canvas.create_oval(*mercure_pos, fill='gray')
venus = canvas.create_oval(*venus_pos, fill='orange')
terre = canvas.create_oval(*terre_pos, fill='blue')
mars = canvas.create_oval(*mars_pos, fill='red')

current_date = start_date
while True :
    current_date = temps.gregorien(temps.JJ(*current_date)+4)

    mercure_old = mercure_pos
    mercure_pos = get_coords(*pos('Mercure', *current_date))
    mercure_dec = get_new(mercure_old, mercure_pos)

    venus_old = venus_pos
    venus_pos = get_coords(*pos('Venus', *current_date))
    venus_dec = get_new(venus_old, venus_pos)

    terre_old = terre_pos
    terre_pos = get_coords(*pos('Terre', *current_date))
    terre_dec = get_new(terre_old, terre_pos)

    mars_old = mars_pos
    mars_pos = get_coords(*pos('Mars', *current_date))
    mars_dec = get_new(mars_old, mars_pos)

    canvas.move(mercure, *mercure_dec)
    canvas.move(venus, *venus_dec)
    canvas.move(terre, *terre_dec)
    canvas.move(mars, *mars_dec)

    canvas.update()
    time.sleep(0.1)
window.mainloop()