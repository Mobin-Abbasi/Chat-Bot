import pyautogui as pg
from time import sleep
from random import choice

lst = ['I Love You', 'I Hate You', 'Hi There', "What's up?", "How Are You?"]
for i in range(5):
    sleep(1)
    pg.click(1111, 963)
    pg.write(choice(lst), interval=0.1)
    pg.press('enter')