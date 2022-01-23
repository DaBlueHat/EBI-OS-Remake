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
        print("glist - lists all of the available games")
        kernel()
    
    if KC == "glist":
        print("snake - snake game")
        gameInput = input("Enter the game a choice: ")

        if gameInput == "snake":
            os.startfile(r'kernel\snake.py')
            kernel()
        
        if gameInput == "exit":
            kernel()

        if gameInput != "snake":
            if gameInput != "exit":
                print("Invalid game input")
                kernel()

    if KC == "shutdown":
        print("Shutting down")
        time.sleep(0.555)
        exit()


    if KC != "help":
        if KC != "web":
            if KC != "shutdown":
                    if KC != "glist":
                        print(KC + " Is a invalid command")
                        kernel()


kernel()