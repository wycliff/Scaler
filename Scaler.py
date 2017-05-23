# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:24:51 2017

@author: Wycliffe
"""

import cv2
from Tkinter import *
from PIL import Image, ImageTk 
import tkFileDialog as tkd  
import tkFont


img_handler=None 
img_file_path=None
path_to_gray= None
#make the UI
#the root and all its characreristics  
root= Tk() 
root.title("GRAY - SCALER")



root.minsize(800,600) #width, height
root.resizable(width=FALSE, height=FALSE)


#The canvas 
canvas=None
#putting canvas
canvas_width =700
canvas_height =500
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.place(x=0,y=0)
canvas.configure(background="#fff")  

  
# opening  the image using a file explorer and getting the path 
def file_opener():
    global root    # Needed to modify global copy of globvar
    #gives the path
    global img_file_path
    file_options = {'initialdir':'/',
                                  'title':'Choose Image',
                                  'filetypes':[('JPEG','*.jpg *.jpeg'),
                                               ('Bitmap Image','*.bmp'),
                                               ('PNG Image','*.png')]}
    
    img_file_path = tkd.askopenfilename(parent=root, **file_options)
    #calls the loadImage function 
    loadImage(img_file_path)
#    my_label= Label(root, text=img_file_path)
#    my_label.pack()
    
    

   
def getFileName(path):
    filestring_split = path.split('/')
    len_split = len(filestring_split)
    filename = filestring_split[len_split-1]
    return filename
    

def getFileExt(file_name):
    name_split = file_name.split(".")
    len_split = len(name_split)
    
    file_ext = name_split[len_split-1]
    return file_ext
        
 
   
def loadImage(file_path):
    #Loading image 
    global canvas
    global img_file_path
    this_image = Image.open(file_path)
    #If the image is bigger than it is resized else it remains the same way
    if(this_image.width * this_image.height > canvas_width * canvas_height ):
        getImage=this_image.resize((canvas_width,canvas_height),Image.ANTIALIAS)#Withpath
    else:
        getImage=this_image 
    #for a useable format of the image    
    myImg = ImageTk.PhotoImage(getImage)
    global img_handler 
    img_handler = canvas.create_image(0,0, anchor=NW,image=myImg) 
    toGray()
    print(img_file_path) 
    
    
def toGray():
    global img_file_path
    print("From ToGray: " + img_file_path)
    cv2.imread(img_file_path)
    gray = cv2.cvtColor(img_file_path,cv2.COLOR_BGR2GRAY)  # To grayScale
    cv2.imshow('Gray-Scaled image', gray)
    cv2.waitKey(0)
    #destroys windows with the click of a button
    cv2.destroyAllWindows() 
    

    
        
def converter():
    global img_file_path
    global path_to_gray
    #    print("From ToGray: " + img_file_path)
    colored_image= cv2.imread(img_file_path,1)
    gray = cv2.cvtColor(colored_image,cv2.COLOR_BGR2GRAY)  # To grayScale
    cv2.imshow('Gray-Scaled image', gray)
    cv2.imwrite('new.png',gray)
    cv2.waitKey(0)
    #destroys windows with the click of a button
    cv2.destroyAllWindows()     
#    Saving the image temporarily
#    the_name=getFileName(img_file_path)
    
       
    
# create a toplevel menu
menubar= Menu(root)
#menubar.add_command(label="FILE")
#menubar.add_command(label="ABOUT")


# create a pulldown menu, and add it to the menu bar
#1)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Load image", command=file_opener)
#filemenu.add_command(label="convert", command = toGray())
filemenu.add_separator()
filemenu.add_command(label="Exit")
#Member of Top Level Menu
menubar.add_cascade(label="File", menu=filemenu)

#2),
aboutMenu = Menu(menubar,tearoff=0)
aboutMenu.add_command(label="Version info")

menubar.add_cascade(label="about", menu= aboutMenu)

#3)
helpMenu = Menu(menubar, tearoff=0)
aboutMenu.add_command(label="how to use this app")

menubar.add_cascade(label="help", menu= helpMenu)

 

# Button to gray scale.
scaler_button = Button(master=root, text="Convert to gray",
                           bg="#2672EC",fg="#ffffff",
                           activebackground ="#19c90e",activeforeground="#FFFFFF",
                           overrelief= GROOVE,
                           cursor="hand2",
                           font=tkFont.Font(size=11), relief=FLAT,command= converter
                           ) 
 
 
scaler_button.place(x=30,y=530) 

#Text View that shows the path of the new gray image
path_to_gray= "Path of the output image"
path_finder= Label(master=root, text=path_to_gray)

path_finder.place(x=200, y=530)
# to display the menu
root.config(menu=menubar)

 
#btn_file_opener.pack(side=TOP, expand=True)
root.configure(background="#000")    
root.mainloop()

 