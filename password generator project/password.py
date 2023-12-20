import string
import random
import pyperclip   # module help to copy and paste
from tkinter import *

# initialize  window

root = Tk()  #add custom command to change and manipulated gui 
root.geometry("700x700") #size of the window

# title of our window
root.title("Random Password Generator")

final_password = StringVar()
pass_len = IntVar()
password_strength= StringVar()


combinations = [string.ascii_lowercase,
    string.ascii_uppercase,
    string.digits,
    string.punctuation]

#-----------------function to generate password

def ranGeneratePass():
    password = ""
    for x in range(pass_len.get()):
        type = random.choice(combinations)
        password = password + random.choice(type)

    final_password.set(password)    
    

#-----------------function to copy password

def copy_password():  
    pyperclip.copy(final_password.get()) 

#------------------function to check password 

def check_password():
    if pass_len.get() <= 4:
        password_strength.set("Password is Bad")
        result_labdel.config(fg="red")
    elif pass_len.get() > 4 and pass_len.get() < 7:
        password_strength.set("Password is Weak")
        result_labdel.config(fg="orange")
    else:
        password_strength.set("password is strong")
        result_labdel.config(fg="green")

#------------------ front-end designing 

lable_head = Label(root, text='Random Password Generator', font='arial 20 bold').pack(pady=15)
length_head = Label(root, text='Enter the length of password', font="arial 12 bold").pack(pady=12)
Entry(root,width=20, font='arial 16', textvariable=pass_len).pack(pady=10)


#--------------------designing  generate button

generate_button = Button(root, command=ranGeneratePass, text = 'Generate Password', padx=12, pady=8, bg='lightblue', fg='black').pack(pady=10)

#----------------------generated password 

output_pass = Label(root, text= 'Your Generated Password', font ='arial 12 bold').pack(pady="30 10")
pass_result=Entry(root, textvariable=final_password, width=24, font='arial 16').pack()

#-------------------------check button
check_button = Button(root, command=check_password, text='check strength',font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=12, pady=8).pack(pady=10)

#--------------------display the password strength
result_labdel=Label(root, textvariable=password_strength, width=24, font='arial 16')
result_labdel.pack(pady=10)

#----------------------copy button

copy_button = Button(root, command=copy_password, text = 'Copy',font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=12, pady=8 ).pack(pady=10)

root.mainloop()






