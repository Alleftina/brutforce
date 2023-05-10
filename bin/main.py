import pyautogui
import time
import keyboard



def main():
    pyautogui.PAUSE = 0.1
    pyautogui.FAILSAFE = True
    pyautogui.size()
    print(pyautogui.position())
    pyautogui.move(100/2,200*2, duration=0.5)
    pyautogui.click()
    # pyautogui.doubleClick()
    # pyautogui.rightClick()
    
    # pyautogui.scroll(-10)
    # pyautogui.middleClick()
    pyautogui.press('enter')
    pyautogui.typewrite('123456', interval=0)
main()