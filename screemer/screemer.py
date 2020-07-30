import pygame
import tkinter as tk
from PIL import Image, ImageTk
from PIL import Image, ImageTk
from itertools import count
import pygame # библиотека, которую мы исопользуем только для звука
import time # для задержки какой-то
import random #для рандомизации задержки



ssw = tk.Tk()
def six():
     pygame.mixer.init()
     pygame.mixer.music.load("1.mp3")
     pygame.mixer.music.set_volume(0.2)
     pygame.mixer.music.play()
     # ssw.configure(background="black")
     image = Image.open("1.gif")
     zoom = 1.8
     pixels_x, pixels_y = tuple([int(zoom * x) for x in image.size])
     toplvl = tk.Toplevel()  # топ левел виджет
     photo = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
     lbl = tk.Label(toplvl, image=photo)
     lbl.image = photo
     lbl.grid(row=0, column=0)

def base():
    la = tk.Button(ssw, text='Не Нажимай сюда', command = six)
    la.grid(row=0, column=0)
base()
ssw.mainloop()