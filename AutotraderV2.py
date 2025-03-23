import pyautogui
import time
import discord
import typing
import asyncio
import functools
canceled = False
#import Autotrader

def to_thread(func: typing.Callable) -> typing.Coroutine:
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        return await asyncio.to_thread(func, *args, **kwargs)
    return wrapper

@to_thread
async def CFC(message):#Check for cancel
    #print("YES IM RUNNING")
    global canceled
    if (pyautogui.locateOnScreen('expired.png', confidence=0.9) != None):
        okCanceled = pyautogui.locateOnScreen('okCanceled.png', confidence=0.9)
        pyautogui.click(pyautogui.center(okCanceled), clicks=1, interval=1)
        await message.channel.send("Trade Expired")
        canceled = True
        #return True
    if (pyautogui.locateOnScreen('unavailable.png', confidence=0.9) != None):
        okCanceled = pyautogui.locateOnScreen('okCanceled.png', confidence=0.9)
        pyautogui.click(pyautogui.center(okCanceled), clicks=1, interval=1)
        await message.channel.send("Unavailable Message")
        canceled = True
        #return True
    if (pyautogui.locateOnScreen('canceled.png', confidence=0.9) != None):
        okCanceled = pyautogui.locateOnScreen('okCanceled.png', confidence=0.9)
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('okCanceled.png', confidence=0.9)), clicks=1, interval=1)
        await message.channel.send("Partner canceled the trade")
        canceled = True
        #return True
    return 

@to_thread
async def trade(message):
    if (canceled == True):return
    trade = pyautogui.locateOnScreen('trade.png', confidence=0.9)
    while (pyautogui.locateOnScreen('trade.png', confidence=0.9) == None) :
        await CFC(message)
        if (canceled == True):return
        print("Waiting for trade menu button")
        time.sleep(0.1)
    while (pyautogui.locateOnScreen('trade.png', confidence=0.9) != None) :
        await CFC(message)
        if (canceled == True):return
        print("Clicking trade button")
        trade = pyautogui.locateOnScreen('trade.png', confidence=0.9)
        #pyautogui.moveTo(pyautogui.center(trade), duration = 0)
        time.sleep(0.3)
        pyautogui.click(pyautogui.center(trade), clicks=1, interval=1)
    next = pyautogui.locateOnScreen('next.png', confidence=0.9)
    while (pyautogui.locateOnScreen('next.png', confidence=0.9) == None):
        print("Selecting pokemon")
        await CFC(message)
        if (canceled == True):return
        time.sleep(0.3)
        pyautogui.click(132, 378, clicks=1, interval=1)
    while (pyautogui.locateOnScreen('next.png', confidence=0.9) != None):
        await CFC(message)
        if (canceled == True):return
        print("Clicking next")
        next = pyautogui.locateOnScreen('next.png', confidence=0.9)
        time.sleep(0.3)
        pyautogui.click(pyautogui.center(next), clicks=1, interval=1)
    while (pyautogui.locateOnScreen('confirm100.png', confidence=0.9) == None):
        await CFC(message)
        if (canceled == True):return
        print("Waiting for partner's choice")
        time.sleep(0.1)
    while (pyautogui.locateOnScreen('confirm100.png', confidence=0.9) != None):
        await CFC(message)
        if (canceled == True):return
        print("Confirming trade for 100 dust")
        confirm100 = pyautogui.locateOnScreen('confirm100.png', confidence=0.9)
        time.sleep(0.3) 
        pyautogui.click(pyautogui.center(confirm100), clicks=1, interval=1) 
    while (pyautogui.locateOnScreen('menu.png', confidence=0.9) == None):
        await CFC(message)
        if (canceled == True):return
        print("Waiting for animation to finish")
        time.sleep(0.1)  
    while (pyautogui.locateOnScreen('menu.png', confidence=0.9) != None):
        await CFC(message)
        if (canceled == True):return
        print("Clicking x to return to friend page")
        time.sleep(0.3)  
        pyautogui.click(294, 886, clicks=1, interval=1)
    await message.channel.send("Finished a trade")
    return

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global canceled
        if (message.author.id != 1114734620156633128):
            #print(message.author.id)
            print(f'Message from {message.author}: {message.content}')
            #print(message.channel)
            if (message.content == ".trade"):
                canceled = False
                await message.channel.send("Recieved, making a trade")
                while True:
                    if (canceled == True):
                        await message.channel.send("Canceled")
                        break
                    await trade(message)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('') # Token here