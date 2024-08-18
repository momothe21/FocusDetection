#This is created by Mohammed Obeidi.
#This is where the face being recorded will be shwon and analyzied in real time.

#imports
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import cv2
import Menu
import Fixing
import Pred

#keeping track
percentages = [0,0,0,0,0,0,0,0]

#switch case function for prediction
def switch_case(case):
    if case == 10:
        percentages[1]+=1
        return "Far left"
    elif case == 41:
        percentages[2]+=1
        return "Medium left"
    elif case == 50:
        percentages[3]+=1
        return "Near left"
    elif case == 51:
        percentages[4]+=1
        return "Straight"
    elif case == 80:
        percentages[5]+=1
        return "Medium right"
    elif case == 90:
        percentages[6]+=1
        return "Far right"
    elif case == 110:
        percentages[6]+=1
        return "Far right"
    elif case == 120:
        percentages[6]+=1
        return "Far right"
    elif case == 130:
        percentages[5]+=1
        return "Medium right"
    elif case == 140:
        percentages[7]+=1
        return "Near right"
    elif case == 190:
        percentages[3]+=1
        return "Near left"
    elif case == 200:
        percentages[1]+=1
        return "Far left"
    elif case == 240:
        percentages[1]+=1
        return "Far left"


#beggining program
def begin():
    #making window
    win = Toplevel()
    win.title("Face analysis")
    win.resizable(False, False)
    win.geometry('+%d+%d' % (510, 50))
    
    #creating label to display results
    resultsLabel = Label(win, text='')
    
    #displaying camera
    #create a Label to capture the Video frames
    camLabel = Label(win)
    camLabel.grid(row=0, column=0)
    cam = cv2.VideoCapture(0)
    
    #define function to show computer camera
    def show_cam():
        #get the latest frame
        gotten, cv2image = cam.read()

        #check if frame is successfully read
        if gotten:
            #convert the frame to RGB
            cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGB)

            #turn the frame into an image
            img = Image.fromarray(cv2image)

            #convert image to PhotoImage
            imgtk = ImageTk.PhotoImage(image=img)
            camLabel.imgtk = imgtk
            camLabel.configure(image=imgtk)
        
        #save the captured frame as an image
            cv2.imwrite("captured_image.jpg", cv2image)

            #cropping, and enhancing on the face from the captured image
            fixed = Fixing.cl()
            
            #checking if a face was seen
            if fixed == False:
                #Editing the label to say no face is found
                resultsLabel.config(text="No Face Detected!")
                resultsLabel.config(font=("Arial", 20))
            else:
                # Edit the label and display the image while deleting any text if it exists
                resultsLabel.config(text= switch_case(int((Pred.predi()))))
                resultsLabel.config(font=("Arial", 20))
        
        else:
            print("No frame captured, error!")
            
        #repeat after an interval to capture continuously
        percentages[0]+=1
        camLabel.after(20, show_cam)
        
    #return to menu function
    def return_to_menu():
        Menu.menu_return()
        win.destroy()
        cam.release()
        
        #printing results to terminal
        print("Percentages for directions")
        print("Far left: %",100*percentages[1]/percentages[0])
        print("Medium left: %",100*percentages[2]/percentages[0])
        print("Near left: %",100*percentages[3]/percentages[0])
        print("Straight: %",100*percentages[4]/percentages[0])
        print("Near right: %",100*percentages[5]/percentages[0])
        print("Medium right: %",100*percentages[6]/percentages[0])
        print("Far right: %",100*percentages[7]/percentages[0])
      
    #label for predictions
    resultsLabel.grid(column=0, row=2, ipadx=10, ipady= 20)  
      
    #creating button to return to the menu
    RT = ttk.Button(win, text="Return to Menu", command=return_to_menu)
    RT.grid(column=0, row=3)
    RT.grid(ipadx=10, ipady=20)

    #begin showing images
    show_cam()
            