#this code depends only on keyboard actions due to lack of locate() functionality as I am using Wayland compositor
import pyautogui
import time as t
import os
def start_search():
    pyautogui.keyDown('ctrl')
    t.sleep(0.5)
    pyautogui.hotkey('shift', 'E')
    t.sleep(0.5)
    pyautogui.keyUp('ctrl')
    t.sleep(0.5)
    pyautogui.keyDown('ctrl')
    t.sleep(1)
    pyautogui.hotkey('shift', 'X')
    t.sleep(1)
    pyautogui.keyUp('ctrl')
    t.sleep(1.5)
def selectAll():
    pyautogui.hotkey('ctrl', 'a')
    t.sleep(.2)
#print(pyautogui.locateOnScreen("bar.png"))
start_search()
selectAll()
pyautogui.typewrite(list("cmake"),0.3)
t.sleep(0.4)
pyautogui.typewrite(['tab','tab','Down','Down', 'tab', 'enter'],0.5)
t.sleep(10)
start_search()
selectAll()
pyautogui.typewrite(list("cmake tools"), 0.2)
pyautogui.typewrite(['tab','tab','Down','Down', 'Down', 'tab', 'enter'],0.5)
t.sleep(10)
start_search()
selectAll()
pyautogui.typewrite(list("clangd"), 0.2)
pyautogui.typewrite(['tab','tab','Down','Down', 'Down', 'tab', 'enter'],0.5)
t.sleep(10)
start_search()
selectAll()
pyautogui.typewrite(list("c++ testmate"), 0.2)
pyautogui.typewrite(['tab','tab','Down', 'tab', 'enter'],0.5)
t.sleep(10)


