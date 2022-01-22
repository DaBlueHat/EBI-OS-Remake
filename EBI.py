import time
import os

time.sleep(0.555)

def bootloaderGraphical():
    print("----------------EBI BOOT MENU----------------")
    print("EBI OS VERSION 0.1")
    os.system("pause")
    bootloaderCode()

def bootloaderCode():
    with open(r'system\boot\bootloader.EBI') as A:
        boot = A.read()

    if boot == "00":
        time.sleep(0.555)
        os.system("cls")
        os.startfile('setup.py')
        exit()

    if boot == "01":
        time.sleep(0.555)
        os.system("cls")
        os.startfile('login.py')
        exit()





bootloaderGraphical()