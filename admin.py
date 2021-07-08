from tkinter import *

root = Tk()
root.title("The Log Connect")
root.geometry("500x500")
root.config(bg="peach puff")

font_style = ("Palatino",14)

username = Label(root, text = "New Username",font=font_style).grid(column = 1,row = 9)
get_name = Entry(root).grid(column=3,row=9)

password = Label(root, text = "New Password",font=font_style).grid(column=1,row=10)
get_pass = Entry(root).grid(column=3,row=10)

password2 = Label(root, text = "Confirm Password",font=font_style).grid(column=1,row=11)
get_pass2 = Entry(root).grid(column=3,row=11)

register_user = Button(root, text ="Register New User", font=font_style, bg="light steel blue").grid(column=2, row=14)

root.mainloop()
