import pyautogui
import pytesseract

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#search = pyautogui.center(pyautogui.locateOnScreen('search.png', confidence=0.9))
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
#text = pytesseract.image_to_string(pyautogui.screenshot(region=(search.x-50,search.y+207,search.x+40,search.y-170)))
#print("You traded: ",text)

confirm100 = pyautogui.center(pyautogui.locateOnScreen('confirm100.png', confidence=0.9))
#img = pyautogui.screenshot(region=(confirm100.x-122,confirm100.y-268,confirm100.x+50,confirm100.y-480))
#img.show()
text = pytesseract.image_to_string(pyautogui.screenshot(region=(confirm100.x-122,confirm100.y-268,confirm100.x+50,confirm100.y-480)))
print("Partner traded: ",text)

#no way it works

#99, 205

#49, 412
#187, 445

#[-50, 207]
#[88, 240]

#165, 518

#43, 250
#242, 285

#-122,-268
#+77,-233

#confirm100.x-122,confirm100.y-268,confirm100.x+77,confirm100.y-233