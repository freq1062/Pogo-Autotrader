import pyautogui
import time
#im = pyautogui.screenshot()
counter = 0

def CFC(c):#Check for cancel
    if (pyautogui.locateOnScreen('canceled.png', confidence=0.9) != None):
        print("Final number of trades: "+str(c))
        exit()

while (pyautogui.locateOnScreen('canceled.png', confidence=0.9) == None):
    trade = pyautogui.locateOnScreen('trade.png', confidence=0.9)
    while (pyautogui.locateOnScreen('trade.png', confidence=0.9) == None) :
        print("Waiting for trade menu button")
        time.sleep(0.1)
    while (pyautogui.locateOnScreen('trade.png', confidence=0.9) != None) :
        print("Clicking trade button")
        trade = pyautogui.locateOnScreen('trade.png', confidence=0.9)
        #pyautogui.moveTo(pyautogui.center(trade), duration = 0)
        time.sleep(0.3)
        pyautogui.click(pyautogui.center(trade), clicks=1, interval=1)
    next = pyautogui.locateOnScreen('next.png', confidence=0.9)
    while (pyautogui.locateOnScreen('next.png', confidence=0.9) == None):
        print("Selecting pokemon")
        CFC(counter)
        time.sleep(0.3)
        pyautogui.click(132, 378, clicks=1, interval=1)
    while (pyautogui.locateOnScreen('next.png', confidence=0.9) != None):
        CFC(counter)
        print("Clicking next")
        next = pyautogui.locateOnScreen('next.png', confidence=0.9)
        time.sleep(0.3)
        pyautogui.click(pyautogui.center(next), clicks=1, interval=1)
    while (pyautogui.locateOnScreen('confirm100.png', confidence=0.9) == None):
        CFC(counter)
        print("Waiting for partner's choice")
        time.sleep(0.1)
    while (pyautogui.locateOnScreen('confirm100.png', confidence=0.9) != None):
        CFC(counter)
        print("Confirming trade for 100 dust")
        confirm100 = pyautogui.locateOnScreen('confirm100.png', confidence=0.9)
        time.sleep(0.3) 
        pyautogui.click(pyautogui.center(confirm100), clicks=1, interval=1) 
    while (pyautogui.locateOnScreen('menu.png', confidence=0.9) == None):
        CFC(counter)
        print("Waiting for animation to finish")
        time.sleep(0.1)  
    while (pyautogui.locateOnScreen('menu.png', confidence=0.9) != None):
        CFC(counter)
        print("Clicking x to return to friend page")
        time.sleep(0.3)  
        pyautogui.click(294, 886, clicks=1, interval=1)
    time.sleep(0.1)
    counter+=1

print(counter)

#confirm100 = pyautogui.locateOnScreen('confirm100.png')
#next = pyautogui.locateOnScreen('next.png')
#pyautogui.moveTo(pyautogui.center(trade), duration = 0)
#time.sleep(0.2)
#pyautogui.click()
#132, 378 location of first pokemon 