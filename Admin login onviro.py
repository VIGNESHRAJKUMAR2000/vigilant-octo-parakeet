from tkinter import *
from tkinter import messagebox
import os
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.iconbitmap('login icon.ico')
    login_screen.title("ONVIRO ( version 1.0 )")
    login_screen.geometry("500x300+700+100")
    
    Label(login_screen, text="Developer Login (admin)",bg="green yellow",width="300",height="1",font=("Berlin Sans FB", 12)).pack()
    Label(login_screen, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="For a period of Support -  following the installation of the Software,",width="300",bg="SkyBlue2").pack()
    Label(login_screen, text="the Developer shall perform its maintenance and support services consistent with generally",width="300",bg="SkyBlue2").pack()
    Label(login_screen, text="accepted industry standards, but only if the Software is installed and operated in accordance",width="300",bg="SkyBlue2").pack()
    Label(login_screen, text="with the Developer's documentation and other instructions.",width="300",bg="SkyBlue2").pack()
    Label(login_screen, text="").pack()
 
    Label(login_screen, text="USERNAME").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="PASSWORD").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", bg="green2",width="8" ,height="1",font=("Aharoni", 10), command = login_verify).pack()
    Label(text="").pack()
 
# Implementing event on login button 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            messagebox.showwarning("Error","Invalid Password")
 
    else:
        messagebox.showinfo("Check","User not found")
 
# Designing popup for login success
def login_sucess():
    login_screen.destroy()
    main_screen.destroy()
    os.system('python onviro.py')
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.iconbitmap('login icon.ico')
    main_screen.geometry("400x150+200+100")
    main_screen.title("ONVIRO ( version 1.0 )")
    Label(text="Administrator Login", bg="orange", width="300", height="2", font=("Andalus", 20)).pack()
    Label(text="").pack()
    Button(text="LOGIN", bg="green2",width="25" ,height="1",font=("Aharoni", 10), command = login).pack()
    Label(text="").pack()
    main_screen.mainloop()
    
 
main_account_screen()
