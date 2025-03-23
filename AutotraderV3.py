import pyautogui
import time
import discord
import functools
import typing
import asyncio
from datetime import datetime
import pytesseract
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

def youTraded(): #unused
    search = pyautogui.center(pyautogui.locateOnScreen('search.png', confidence=0.9))
    text = pytesseract.image_to_string(pyautogui.screenshot(region=(search.x-50,search.y+207,search.x+40,search.y-170)))
    return "You traded: ",text

def partnerTraded(): #unused
    confirm100 = pyautogui.center(pyautogui.locateOnScreen('confirm100.png', confidence=0.9))
    text = pytesseract.image_to_string(pyautogui.screenshot(region=(confirm100.x-122,confirm100.y-268,confirm100.x+50,confirm100.y-480)))
    return "Partner traded: ",text

def CFC():#Check for cancel, expired, error, or limit reached
    canceled = False
    if (pyautogui.locateOnScreen('limit.png', confidence=0.9) != None):
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('okCanceled.png', confidence=0.9)), clicks=1, interval=1)
        print("Daily limit reached", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        canceled = True
    if (pyautogui.locateOnScreen('expired.png', confidence=0.9) != None):
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('okCanceled.png', confidence=0.9)), clicks=1, interval=1)
        print("Trade expired", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        canceled = True
    if (pyautogui.locateOnScreen('unavailable.png', confidence=0.9) != None):
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('okCanceled.png', confidence=0.9)), clicks=1, interval=1)
        print("Trading service unavailable", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        canceled = True
    if (pyautogui.locateOnScreen('canceled.png', confidence=0.9) != None):
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('okCanceled.png', confidence=0.9)), clicks=1, interval=1)
        print("Partner canceled", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        canceled = True
    return canceled

def to_thread(func: typing.Callable) -> typing.Coroutine: #Since the trade blocks discord's "heartbeat" this coroutine manager is nessecary
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        return await asyncio.to_thread(func, *args, **kwargs)
    return wrapper

@to_thread
def interact(img, location, message): #Wait for one action in the trade process
    while (pyautogui.locateOnScreen(str(img), confidence=0.8) == None):
        if (CFC()):
            return True
        time.sleep(0.1)
    print(message, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    if (location == "center"):
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(str(img), confidence=0.8)), clicks=1, interval=1)
    else:
        imgCoords = pyautogui.center(pyautogui.locateOnScreen(str(img), confidence=0.8))
        pyautogui.click(imgCoords.x+location[0], imgCoords.y+location[1], clicks=1, interval=1)
    return False

@to_thread
def confirm(): #Special function for confirming since partner can "unpress" the button by reselecting
    while (pyautogui.locateOnScreen(str("menu.png"), confidence=0.8) == None):
        if (CFC()): 
            return True
        if (pyautogui.locateOnScreen(str("confirm100.png"), confidence=0.8) == None):
            time.sleep(0.1)
        else:
            print("Confirmed", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("confirm100.png", confidence=0.8)), clicks=1, interval=1)
    return False

class MyClient(discord.Client): #Main event loop for discord.py
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if (message.author.id != 1114734620156633128):
            print(f'Message from {message.author}: {message.content}')
            if (message.content == ".trade"):
                await message.channel.send("Recieved, making a trade")
                while True:
                    print("Starting")
                    if (await interact("trade.png", "center", "Trade button")):break
                    if (await interact("search.png", [16, 161], "Select pokemon")):break
                    if (await interact("next.png", "center","Next")):break
                    if (await confirm()): break
                    if (await interact("menu.png", [-182, 4], "Return to friend")):break
                    await message.channel.send("Made a trade")
                    
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('') # Token here