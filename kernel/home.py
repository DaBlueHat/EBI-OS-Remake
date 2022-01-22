import os
import time

def kernel():
    KC = input("Enter a command to execute: ")

    if KC == "web":
        os.startfile(r'kernel\web.py')
        exit()

    if KC == "help":
        print("help - displays the help information")
        print("web - opens the web browser")
        print("shutdown - shuts down the os")
        kernel()
    
    if KC == "shutdown":
        print("Shutting down")
        time.sleep(0.555)
        os.startfile('shutdown.py')
        exit()

    if KC != "help":
        if KC != "web":
            if KC != "shutdown":
                print(KC + " Is a invalid command")
                kernel()


kernel()