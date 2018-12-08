from tkinter import *

root = Tk()
username = Label(root, text="User Name")
password = Label(root, text="Password")
name_entry = Entry(root)  # input field
pass_entry = Entry(root)  # input field

username.grid(row=0, sticky=E)  # bydefault column=0   NEWS
password.grid(row=1, sticky=E)
name_entry.grid(row=0, column=1)
pass_entry.grid(row=1, column=1)

#  -------------------------- image -----------------------
logo = PhotoImage(file="pepsi.png")
logolabel = Label(root, image=logo)
logolabel.grid(row=2, column=2)

check = Checkbutton(root, text="Keep me logged in")
check.grid(columnspan=2)
root.mainloop()
