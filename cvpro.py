import tkinter as tk
from PIL import Image , ImageTk ,ImageFilter
import cv2
import os,sys
def getn():
    name=name_var.get()
    roll=roll_var.get()
    print(name)
    name_var.set("hello")
    return name

def getinp():
    f1=tk.Tk()
    f1.geometry("500x500")
    name_entry=tk.Entry(f1,textvariable=name_var)
    roll_entry=tk.Entry(f1,textvariable=roll_var)
    name=getn()
    name_entry.place(x=10,y=50)
    roll_entry.place(x=10,y=100)
    b1=tk.Button(f1,text="Take IMAGE",command=lambda:enterdata(name),background="white",foreground="black",font=("Century Schoolbook",20))
    b1.place(x=10,y=300)
    f1.mainloop()

def enterdata(name):
    haar_file = 'C:\\Users\\DEEPU\\Downloads\\haarcascade_frontalface_default.xml' 
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0)
    count=0
    (width, height) = (130, 100) 
    sub_data = name   
    datasets = 'C:\\Users\\DEEPU\\Downloads\\datasets'
    path = os.path.join(datasets, sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)
    while count<30:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
            cv2.imwrite('% s/% s.png' % (path, count), face_resize)
        count += 1
        cv2.imshow('FaceDetection', im)
        key = cv2.waitKey(500)
        if key == 27:
            break
    webcam.release()
    cv2.destroyAllWindows()
top=tk.Tk()
top.geometry("1200x1500")
name_var=tk.StringVar()
roll_var=tk.IntVar()

bg=Image.open("C:\\Users\\DEEPU\\Downloads\\bg1.png")
bg=bg.resize((1200,800))
bg=bg.filter(ImageFilter.BoxBlur(5))
bg=ImageTk.PhotoImage(bg)
bglabel=tk.Label(top,image=bg)
l1=tk.Label(top,text=".......ATTENDANCE PLATFORM.......")
l1.config(font=("Times",32,'bold'),foreground="blue",background=None)
b1=tk.Button(top,text="FEED DATA",command=lambda:getinp(),background="white",foreground="black",font=("Century Schoolbook",20))
b1.place(x=200,y=350)
l1.place(x=200,y=100)
bglabel.place(x=0,y=0)
top.mainloop()