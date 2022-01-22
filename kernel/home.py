import os
import time
import webbrowser

def kernel():
    KC = input("Enter a command to execute: ")

    if KC == "web":
        os.startfile('web.py')
        exit()

    if KC == "help":
        print("help - displays the help information")
        print("web - opens the web browser")
        print("shutdown - shuts down the os")
    
    if KC == "shutdown":
        print("Shutting down")
        time.sleep(0.555)
        os.startfile('shutdown.py')


kernel()