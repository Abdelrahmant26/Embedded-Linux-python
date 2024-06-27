import os
import pyautogui
print(os.getcwd())
pyautogui.FAILSAFE = True
os.system("grim out.png")
x=pyautogui.locate("chech.png","out.png", confidence=0.9)
print(pyautogui.position())
print(x)
#print(y)
pyautogui.move(200, 200,5)
print(pyautogui.position())