import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

def low():
	entry.delete(0, END)
	length = var1.get()

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = ""
	
	if var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(lower)
		return password
	
	elif var.get() == 0:
		for i in range(0, length):
			password = password + random.choice(upper)
		return password

	elif var.get() == 3:
		for i in range(0, length):
			password = password + random.choice(digits)
		return password
	else:
		print("Please choose an option")

def generate():
	password1 = low()
	entry.insert(10, password1)

def copy1():
	random_password = entry.get()
	pyperclip.copy(random_password)

root = Tk()
var = IntVar()
var1 = IntVar()

tit=Label(root,text="Random Password Generator",font="normal 15 bold")
tit.grid(row=0,column=1,sticky="n")
root.title("Random Password Generator")
style=Style(root)
Random_password = Label(root, text="Password")
Random_password.grid(row=3)
entry = Entry(root)
entry.grid(row=3, column=1)

c_label = Label(root, text="Length")
c_label.grid(row=1)

copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=3, column=2,sticky='s')
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=4, column=1,sticky='s')

radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=2, column=0, sticky='s')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=2, column=1, sticky='s')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=2, column=2, sticky='s')
combo = Combobox(root, textvariable=var1)

combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

root.mainloop()
