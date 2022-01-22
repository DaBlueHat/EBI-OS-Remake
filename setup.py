import time
# import time
import os

with open(r'system\User\username.EBI', 'r+') as A:
    user = input("Enter the name you want: ")
    A.writelines(user)

with open(r'system\User\password.EBI', 'r+') as B:
    pas = input("Enter your password: ")
    B.writelines(pas)

with open(r'system\boot\bootloader.EBI', 'r+') as C:
    C.writelines('01')

os.startfile('EBI.py')