from tkinter import *

# initializing tkinter
root = Tk()
root.title("Registration Form")
root.geometry("750x426")
root.config(bg="antique white")

font_stylize = ("Arial",14)

title = Label(root, text="Registration Form",font=font_stylize,bg="royalblue").grid(column=2,row=1)

name = Label(root, text = "Name:",font=font_stylize).grid(column = 1,row = 3)
get_name = Entry(root).grid(column=3,row=3)

surname = Label(root, text = "Surname:",font=font_stylize).grid(column=1,row=4)
get_surname = Entry(root).grid(column=3,row=4)

id_no = Label(root, text = "ID No: ",font=font_stylize).grid(column = 1,row = 5)
get_id = Entry(root).grid(column=3,row=5)

phone_no = Label(root, text = "Phone No:",font=font_stylize).grid(column = 1,row = 6)
get_phone = Entry(root).grid(column=3,row=6)

nextofkin_name = Label(root, text = "Next of Kin's Name:",font=font_stylize).grid(column=1,row=7)
get_nokn = Entry(root).grid(column=3,row=7)

nextofkin_no = Label(root, text = "Next of Kin's Phone No: ",font=font_stylize).grid(column = 1,row = 8)
get_nokn2 = Entry(root).grid(column=3,row=8)

register_user = Button(root, text ="Register New User", font=font_stylize, bg="light steel blue").grid(column=2, row=14)

root.mainloop()
