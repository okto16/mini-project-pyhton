import pyautogui
import time

message ="STOP!!"
n = 10000
time.sleep(2)

for i in range(n):
    pyautogui.typewrite(message +"\n")