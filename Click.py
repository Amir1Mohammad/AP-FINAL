import pyautogui
import time


screenWidth , screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

def koor(address):

    address = str(address)
    time.sleep(2)
    pyautogui.moveTo(400,45)
    pyautogui.click()
    pyautogui.typewrite(address, interval=0.10)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.moveTo(380,270)
    time.sleep(1)
    pyautogui.click()

    print "OK !"
    print "Welcome To The ",address
    pyautogui.click()
    print "Now You Can Type . OK lets GO"
    print "field ha ro behesh begoo ."


koor('file:///D:/Final%20AP/Comment.html')



'''
koor('www.yahoo.com')
koor('www.bing.com')
koor(www.aparat.com)
koor(www.aparat.com)
'''
