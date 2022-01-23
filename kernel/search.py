import time
import os
import webbrowser

def SearchPath():
    print("--------------------------------SEARCH INTO GOOGLE--------------------------------")
    print("type exit to exit the program and return to the kernel")
    print("For every space type +")
    
    global search
    search =input("Please enter your search: ")

    if search == "exit":
        time.sleep(0.555)
        os.startfile(r'kernel\home.py')

    if search != "exit":
        openBrowser()

def openBrowser():
    print("Loading ")
    global links
    global search
    link = search   
    print("Link : " + link) 
    # https://www.bing.com/search?q=jeff+Bezos&cvid=69cd1afe97134c3ea474ebbe4e5ccb76&aqs=edge.0.69i59l2j0l7.592j0j1&pglt=675&FORM=ANSPA1&PC=U531 
    # Used as base for search
    webbrowser.open('https://www.bing.com/search?q=' + link + '&cvid=69cd1afe97134c3ea474ebbe4e5ccb76&aqs=edge.0.69i59l2j0l7.592j0j1&pglt=675&FORM=ANSPA1&PC=U531 ')



SearchPath()