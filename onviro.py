#-----------------------------------------------O_N_V_R_I_O----------------------------------------------
import os
import cv2
import tempfile
import win32api
import win32print
from datetime import datetime
import time
import serial
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
from tkinter.filedialog import asksaveasfile 
import threading

a=Tk()
a.iconbitmap('onviro icon.ico')
a.title('ONVIRO (version 1.0)')
a.configure(bg='mint cream')
a.geometry('600x400+400+200')

Label1 = Label(a)
logo= PhotoImage(file="ONVIRO.png")
Label1.configure(image=logo)
Label1.configure(text='''Label''')
Label1.pack()

# Progress bar widget 
progress = Progressbar(a, orient = HORIZONTAL,length =450, mode = 'determinate')

def object1():
  global switch  
  switch = True
  print ('\nTeaching Model 1\n')   
  blink1()
  
def object2():
  global switch  
  switch = True
  print ('\nTeaching Model 2\n')   
  blink2()

def camera_test():
    os.system('camera.py')

# Function responsible for the updation of the progress bar value
def on():
  import time
  progress['value'] = 30
  a.update_idletasks() 
  time.sleep(1) 

  progress['value'] = 60
  a.update_idletasks() 
  time.sleep(1) 

  progress['value'] = 90
  a.update_idletasks() 
  time.sleep(1) 
  progress['value'] = 100

  global switch  
  switch = True
  print ('\nStarting Camera\n')   
  blink()

progress.pack(pady = 4)
  
def off():
 camera=cv2.VideoCapture(1)
 camera.release() 
 print ('\nCAMERA OFF\n')
 global switch  
 switch = False

def  print_output():
    print('Printing Output')
    os.startfile("onviro_output.txt", "print")
    time.sleep(3)
    os.remove('onviro_output.txt')

def calc():
  print("Starting image classifier")
                                                                                           
button1=Button(text="Test Camera",width=15,command=camera_test).pack(side=TOP)
button2=Button(text="Start Camera",width=15,command=on).pack(pady=10,side=TOP)
button3=Button(text="Teach Object 1",width=20,command=object1).pack(side=LEFT)
button4=Button(text="Teach Object 2",width=20,command=object2).pack(side=RIGHT)
button5=Button(text="Stop",width=15,command=off).pack(side=TOP)
button6=Button(text="Calculate",width=15,command=calc).pack(side=TOP)
button7=Button(text="Print Output",width=20,command=print_output).pack(side=TOP)
button8=Button(text="Exit",width=15,command=a.destroy).pack(side=BOTTOM)

store2 = 'live'
#--------------------------------------------------------------------------------------
def blink():
 def run():
   camera=cv2.VideoCapture(0)
   m=0
   n=1
   camera.set(cv2.CAP_PROP_FRAME_WIDTH, 940)
   camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)
       
   if not camera.isOpened():
      messagebox.showinfo("ONVIRO","Select the Correct Webcam Port")
      time.sleep(0.25)
      messagebox.showwarning("Error","Could not able to open the Webcam")   
      raise Exception("\nCOULD NOT OPEN THE WEBCAM")

   while (switch == True):
       
     nTime = time.strftime("%d-%m-%Y")
     source = 'products/'
     dest = os.path.join(source+nTime)
     if not os.path.exists(dest):
       os.makedirs(dest) #creat dest dir       
     if (n==1):
       print("CAMERA ON")   

      # Set properties. Each returns === True on success (i.e. correct resolution)   
       Time = time.strftime("  %d-%m-%Y  %I-%M-%S %p")
      
       text_time = time.strftime("Product-"+str(m)+" date: %d-%m-%Y   time: %I-%M-%S %p\n\n")

       # Read picture. ret === True on success
       ret, image= camera.read()
       print (Time)
       cv2.imwrite(os.path.join(dest,"Product-"+str(m)+Time+".png"),image)
       cv2.imwrite(os.path.join(store2,"New.jpg"),image)
       print("Captured Image\n")
       m+=1

       appendFile=open('onviro_output.txt','a')
       appendFile.write(text_time)
            
       time.sleep(3)
       
      
     if switch == False:
       break
 thread = threading.Thread(target=run)  
 thread.start()

#--------------------------------------------------------------------------------------
def blink2():
 def run():
  camera=cv2.VideoCapture(0)
  m=0
  n=1
  store1 = 'object2'
  camera.set(cv2.CAP_PROP_FRAME_WIDTH, 940)
  camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)

  if not camera.isOpened():
      messagebox.showinfo("ONVIRO","Select the Correct Webcam Port")
      time.sleep(0.25)
      messagebox.showwarning("Error","Could not able to open the Webcam")   
      raise Exception("\nCOULD NOT OPEN THE WEBCAM")
          
  while (switch == True):
    if (n == 1):
      print("CAMERA ON")

      # Set properties. Each returns === True on success (i.e. correct resolution)   
      currentTime = datetime.now()
      Time = time.strftime("  %d-%m-%Y  %I-%M-%S %p")
      
      # Read picture. ret === True on success
      ret, image= camera.read()
      print (Time)
      cv2.imwrite(os.path.join(store1,"Object1-"+str(m)+Time+".jpg"),image)
      cv2.imwrite(os.path.join(store2,"New.jpg"),image)
      print("Captured Image\n")
      m+=1
      time.sleep(3)
      
    if switch == False:
      break
 thread = threading.Thread(target=run)  
 thread.start()
 
#--------------------------------------------------------------------------------------
def blink1():
 def run():
  camera=cv2.VideoCapture(0)
  m=0
  n=1
  store1 = 'object1'
  camera.set(cv2.CAP_PROP_FRAME_WIDTH, 940)
  camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)

  if not camera.isOpened():
      messagebox.showinfo("ONVIRO","Select the Correct Webcam Port")
      time.sleep(0.25)
      messagebox.showwarning("Error","Could not able to open the Webcam")   
      raise Exception("\nCOULD NOT OPEN THE WEBCAM")
          
  while (switch == True):
    if (n == 1):
      print("CAMERA ON")

      # Set properties. Each returns === True on success (i.e. correct resolution)   
      currentTime = datetime.now()
      Time = time.strftime("  %d-%m-%Y  %I-%M-%S %p")
      
      # Read picture. ret === True on success
      ret, image= camera.read()
      print (Time)
      cv2.imwrite(os.path.join(store1,"Object1-"+str(m)+Time+".jpg"),image)
      cv2.imwrite(os.path.join(store2,"New.jpg"),image)
      print("Captured Image\n")
      m+=1
      time.sleep(3)
      
    if switch == False:
      break
 thread = threading.Thread(target=run)  
 thread.start()
 
a.mainloop()

