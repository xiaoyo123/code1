import win32gui
import pyautogui as ag

A,B,C,D=(1364,624),(1489,572),(1604,602),(1731,618)

def start(click):
    R,G,B=ag.pixel(click[0],click[1])
    if (R,G,B)==(49, 158, 198):
        return True
    else:
        return False

def isBlack(pos):
    R,G,B=ag.pixel(pos[0],pos[1])
    if (R,G,B)==(0,0,0):
        return True
    else:
        return False

while True:
    if start(A)==True:
        ag.typewrite('1')
    if start(B)==True:
        ag.typewrite('2')
    if start(C)==True:
        ag.typewrite('3')
    if start(D)==True:
        ag.typewrite('4')
    if isBlack(A)==True:
        ag.typewrite('1')
    if isBlack(B)==True:
        ag.typewrite('2')
    if isBlack(C)==True:
        ag.typewrite('3')
    if isBlack(D)==True:
        ag.typewrite('4')