#This is created by Mohammed Obeidi.
#This is the code in charge of the menu operations

#imports
from tkinter import *
from tkinter import ttk
import Help

def start():
    #creating starting window
    global menu
    menu = Tk()
    menu.title("Menu")
    menu.resizable(False, False)
    
    #dimensions for window
    w = 250 
    h = 200

    #get screen width and height
    ws = menu.winfo_screenwidth() 
    hs = menu.winfo_screenheight()

    #calculate x and y coordinates to center window on all computers
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    #set the dimensions of the screen and where it is placed
    menu.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #Create the frame for the menu
    opti = ttk.Frame(menu)
    opti.pack(side=TOP)


    #Button functions        
    #help button
    def open_help():
        menu.withdraw()
        Help.description()
        
    #quit button
    def quit_program():
        menu.quit()
        menu.destroy()
        exit()

    #Buttons
    #Start
    ST = ttk.Button(opti, text="Capture face")
    ST.grid(column=0, row=0)
    ST.grid(ipadx=10, ipady=20)

    #Help
    HE = ttk.Button(opti, text="Help", command=open_help)
    HE.grid(column=0, row=1)
    HE.grid(ipadx=10, ipady=20)

    #Quit
    Q = ttk.Button(opti, text="Quit", command=quit_program)
    Q.grid(column=0, row=2)
    Q.grid(ipadx=10, ipady=20)

    #Start the main event loop
    menu.mainloop()
    
#Return to menu
def menu_return():
    menu.deiconify()