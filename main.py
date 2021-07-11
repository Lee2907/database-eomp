# Life Choices Online - Lihle Buka

import tkinter as tk
import mysql.connector
from tkinter import messagebox

def submitact():

    user = get_name.get()
    passw = get_pass.get()

    print(f"The name entered by you is {user} {passw}")

    logintodb(user, passw)

def logintodb(user, passw):

    # If paswword is enetered by the
    # user
    if passw:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     password = passw,
                                     db ="lifechoicesonline")
        cursor = db.cursor()

    # If no password is enetered by the
    # user
    else:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     db ="lifechoicesonline")
        cursor = db.cursor()

    # A Table in the database
    savequery = "select * from lifechoicesonline"

    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()

        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        print("Query Excecuted successfully")

    except:
        db.rollback()
        print("Error occured")

def register():
    messagebox.showinfo("You have chosen to register as a new user. You may proceed.")
    root.destroy()
    import register
def exit():
    root.destroy()

# initializing tkinter
root = tk.Tk()
root.title("The Log Connect")
root.geometry("775x426")
root.config(bg="peach puff")

#personalized font
font_stylize = ("Georgia",12)
#structure of the form
usernname = tk.Label(root, text = "Please input username",font=font_stylize).grid(column = 1,row = 3)
get_name = tk.Entry(root).grid(column=3,row=3)

password = tk.Label(root, text = "Please input password",font=font_stylize).grid(column=1,row=4)
get_pass = tk.Entry(root).grid(column=3,row=4)

#the buttons
play = tk.Button(root,text = "Login",font=font_stylize,bg="coral",command=logintodb).grid(column=2,row=12)
register_user = tk.Button(root, text ="Register New User", font=font_stylize, bg="coral",command=lambda submitact:logintodb).grid(column=4, row=12)
admin_log = tk.Button(root, text = "Log In As Admin",font=font_stylize,bg="coral").grid(column=3,row=12)
exit = tk.Button(root, text = "Exit", font=font_stylize, bg="coral",command=exit).grid(column=2,row=14)


#starting the form
root.mainloop()
