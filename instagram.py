from tkinter import *

import tkinter.messagebox as tmsg

def about():
    tmsg.showinfo("About Us", "This app version has been tested so many times.If you still had any problems , Contact the developer.\n App Developer: Parveen")

def contact():
    tmsg.showinfo("Contact Us", "Our Company's toll Free number is: \n\t 1800 XXX XXXX")
def e():
    en = ["English"]
    return en

def h():
    hi = ["Hindi"]
    return hi
def s():
    sp = ['Spanish']
    return sp
def f():
    fr = ['French']
    return fr
def c():
    ch = ['Chinese']
    return ch

def total():
    j = e()
    k = h()
    l = s()
    m = f()
    n = c()
    z = j + k + l + m + n
    print(z)
    return z

def getval():
    us = user_val.get()
    pa = pass_val.get()
    print(us)
    print(pa)

root = Tk()
root.geometry("500x555")
root.wm_iconbitmap('instagram.ico')
root.maxsize(width=500, height=555)
root.minsize(width=500, height=555)
root.title("Instagram")
v1 = IntVar()
v1.set(1)
your_menu = Menu(root)
m1 = Menu(your_menu, tearoff=0)
m1.add_checkbutton(label="English", onvalue=1, variable=v1, command=e)
m1.add_checkbutton(label="Hindi", onvalue=2, variable=v1)
m1.add_checkbutton(label="Spanish", onvalue=3, variable=v1)
m1.add_checkbutton(label="French", onvalue=4, variable=v1)
m1.add_checkbutton(label="Chinese", onvalue=5, variable=v1)
m1.add_separator()
m1.add_command(label="Exit", command=quit)

m2 = Menu(your_menu, tearoff=0)
m2.add_command(label="About us", command=about)
m2.add_command(label="Contact us", command=contact)

root.config(menu=your_menu, bg='white')
your_menu.add_cascade(label="Language", menu=m1)
your_menu.add_cascade(label="Help", menu=m2)
x = total()
Label(text="English", bg='white', font=("comicsans", 10)).pack()
photo = PhotoImage(file='insta_h copy.png')
my = Label(root, image=photo, bg='white')
my.pack(pady=20)

Button(root, text="    f  Continue with Facebook    ",
       fg='white', bg='blue', font=("Arial Black", 9)).pack()

Label(text="--------------------    OR    --------------------", font=("Arial Black", 10), bg='white').pack(pady=15)

user_val = StringVar()
pass_val = StringVar()
user_val.set('Username')
pass_val.set('Password')
u = Entry(root, textvariable=user_val, width=40, borderwidth=4, relief=SUNKEN)
u.pack(pady=15)
p = Entry(root, textvariable=pass_val, width=40, borderwidth=4, relief=SUNKEN)
p.pack()

Label(text="\n\t\t\tForgot password?\n", bg='white', fg='blue').pack()

Button(text="Log In", fg='white', bg='sky blue', width=30, command=getval).pack()

Label(text="\nDon't have an account?", bg='white', font=("Arial Black", 10)).pack()
Label(text="\t\tSign Up", bg='white', fg='blue', font=("Arial Black", 10)).pack()

Label(text="\n\n\n\n\nfrom", bg='white', font=("comicsans", 9)).pack()
Label(text="FACEBOOK", bg='white', font=("Arial Black", 12)).pack()

root.configure(bg='white')
root.mainloop()
