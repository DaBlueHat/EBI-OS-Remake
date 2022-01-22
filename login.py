import time
import os

time.sleep(0.555)

with open(r'system\User\username.EBI') as A:
    rightpass = A.read()
    unlock = input("Enter password: ")

    if unlock == rightpass:
        print("The system is unlocked")
        time.sleep(0.555)
        os.startfile(r'kernel\home.py')

    if unlock != rightpass: 
        print("Wrong password entered")
        os.startfile('login.py')
