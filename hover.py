from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while True:
    print('Waiting...')
    time.sleep(8)

while 1:
    if pyautogui.locateOnScreen('viking.png', grayscale=True, confidence=0.8) != None:
        print('I can see the Viking')
    else:
        None

while 2:
    if pyautogui.locateOnScreen('astronaut.png', grayscale=True, confidence=0.8) != None:
        print('I can see it the astro')
    else:
        None

while 3:
    if pyautogui.locateOnScreen('camper.png', grayscale=True, confidence=0.8) != None:
        print('I can see the camper')
    else:
        None

while 4:
    if pyautogui.locateOnScreen('cowboy.png', grayscale=True, confidence=0.8) != None:
        print('I can see the cowbot')
    else:
        None

while 8:
    if pyautogui.locateOnScreen('fisherman.png', grayscale=True, confidence=0.8) != None:
        print('I can see the fisherman')
    else:
        None

while 6:
    if pyautogui.locateOnScreen('galaxy.png', grayscale=True, confidence=0.8) != None:
        print('I can see the galaxy')
    else:
        None

while 7:
    if pyautogui.locateOnScreen('skeleton.png', grayscale=True, confidence=0.8) != None:
        print('I can see the skeleton')
    else:
        None

while 8:
    if pyautogui.locateOnScreen('sunflower.png', grayscale=True, confidence=0.8) != None:
        print('I can see the sunflower')
    else:
        None

while 9:
    if pyautogui.locateOnScreen('tennis.png', grayscale=True, confidence=0.8) != None:
        print('I can see the tennis')
    else:
        None

while 10:
    if pyautogui.locateOnScreen('tourist.png', grayscale=True, confidence=0.8) != None:
        print('I can see the tourist')
    else:
        print('I cant see it')

while 11:
    if pyautogui.locateOnScreen('player.png', grayscale=True, confidence=0.8) != None:
        print('I can see the player')
    else:
        None
while 1:
    if pyautogui.locateOnScreen('shootem.png', grayscale=True, confidence=0.8) != None:
        print('I can see The Shootem')
    else:
        None

'''
        win32api.SetCursorPos((x, grayscale=True,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, grayscale=True,0, grayscale=True,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, grayscale=True,0, grayscale=True,0)
        '''
'''
def click(x, grayscale=True,y):
    win32api.SetCursorPos((x, grayscale=True,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, grayscale=True,0, grayscale=True,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, grayscale=True,0, grayscale=True,0)
'''