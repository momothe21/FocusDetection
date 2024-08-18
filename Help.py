#This program is created by Mohammed Obeidi
#This is to create the description/help window

#imports
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import Menu

#function
#creating describtion window
def description():
   #creating the new window and centering it
   helpWindow = Toplevel()
   helpWindow.title("Project Description")
   helpWindow.geometry('+%d+%d' % (510, 50))
   helpWindow.resizable(False, False)
   
   #Making the info
   #Create the explain window's text
   exp = Label(helpWindow, text="This Program is created by Mohammed Obeidi.\n The purpose was to use the program to identify where the attention of a student is directed in real time.\n Simply click on capture face and it will begin analysing the focus.\nThe analysis will be posted in terminal.")
   exp.grid(column=0, row=0)
   exp.grid(ipadx=15, ipady=15)
   
   #Load and display an image
   im1 = ImageTk.PhotoImage(Image.open("images\FaceDirectionImage.png"))

   #Create a label and display the image
   l1 = Label(helpWindow, image=im1)
   l1.image = im1
   l1.grid(column=0, row=1)
   
   #creating function to return
   def return_to_menu():
      Menu.menu_return()
      helpWindow.destroy()
   
   #Creating button to return to menu
   RT = ttk.Button(helpWindow, text="Return to Menu", command=return_to_menu)
   RT.grid(column=0, row=3)
   RT.grid(ipadx=10, ipady=20)