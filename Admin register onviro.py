from tkinter import *
from tkinter import messagebox
import os
import time 
# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.iconbitmap('login icon.ico')
    register_screen.title("ONVIRO ( version 1.0 )")
    register_screen.geometry("500x280+200+300")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="For a period of Support -  following the installation of the Software,",width="300",bg="SkyBlue2").pack()
    Label(register_screen, text="the Developer shall perform its maintenance and support services consistent with generally",width="300",bg="SkyBlue2").pack()
    Label(register_screen, text="accepted industry standards, but only if the Software is installed and operated in accordance",width="300",bg="SkyBlue2").pack()
    Label(register_screen, text="with the Developer's documentation and other instructions.",width="300",bg="SkyBlue2").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="USERNAME")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="PASSWORD")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", bg="yellow2",width="8" ,height="1",font=("Aharoni", 10), command = register_user).pack()
    
# Implementing event on register button
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(register_screen, text="Registration Successful", fg="green", font=("calibri", 14)).pack()
    
# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.iconbitmap('login icon.ico')
    main_screen.geometry("400x150+200+100")
    main_screen.title("ONVIRO ( version 1.0 )")
    Label(text="Admin Registration", bg="red", width="300", height="2", font=("Andalus", 20)).pack()
    Label(text="").pack()
    Button(text="REGISTER", bg="green2",width="25" ,height="1",font=("Aharoni", 10), command=register).pack()
    main_screen.mainloop()
 
main_account_screen()
