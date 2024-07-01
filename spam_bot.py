import pyautogui
import time

time.sleep(10)

def message():
    pyautogui.write("This is spam message")
    pyautogui.press('enter')

while True:
    message()
    time.sleep(1)  