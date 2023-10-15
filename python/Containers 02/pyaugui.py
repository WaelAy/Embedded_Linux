import pyautogui
import os
import time
os.system("code")

time.sleep(2)

list_Extentions = ["clangd","c++ testmate","c++ helper","cmake","cmake tools"]

#while(1):
    #pyautogui.mouseInfo()

#full screen
pyautogui.press("f11")
pyautogui.hotkey("ctrl","shift","x")
for i in list_Extentions:
    
    

    pyautogui.write(i)
    time.sleep(5)
    pyautogui.moveTo(218,203)
    pyautogui.leftClick()
    pyautogui.moveTo(196,100)
    pyautogui.leftClick()
    pyautogui.leftClick()
    pyautogui.hotkey("ctrl","a")
    pyautogui.press("backspace")
    

pyautogui.press("f11")
pyautogui.hotkey("alt","f4")
