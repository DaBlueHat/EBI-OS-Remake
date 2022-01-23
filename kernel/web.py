import webbrowser
import time
import os

def web():
    global wwwlink
    print("--------------------------------WEB BROWSER--------------------------------")
    print("type exit to exit the application and return to the kernel")
    print("type search to open the search")
    global wwwInput
    wwwInput = input("LINK : ")
    wwwlink = wwwInput
    print("WEB LINK = " + wwwlink)
    time.sleep(1)

    if wwwInput == "exit":
        print("goodbye")
        time.sleep(1)
        os.startfile(r'kernel\home.py')

    if wwwInput == "search":
        os.startfile(r'kernel\search.py')


    if wwwInput != "exit":
        if wwwInput != "search":
            openBrowser()



def openBrowser():
    webbrowser.open(wwwlink)
    web()


web()