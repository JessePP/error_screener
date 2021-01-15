from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pyscreeze
count = 0

while True:
    if pyautogui.locateOnScreen('Picure.jpg', region=(0,0,1920,1080),  confidence=0.8) !=None:
        count = count + 1
        im2 = pyautogui.screenshot('my_screenshot{}.png'.format(count))
        time.sleep(2)
        _Ok_button_ = pyautogui.locateOnScreen('E:/projekty/ifapears/Ok-buttom.jpg', region=(0,0,1920,1080),  confidence=0.8)
        pyautogui.click(_Ok_button_)
        print(count)
