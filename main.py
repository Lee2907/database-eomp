import tkinter as tk

# initializing tkinter
root = tk.Tk()
root.title("The Log Connect")
root.geometry("775x426")
root.config(bg="peach puff")

font_stylize = ("Verdana",11)

name = tk.Label(root, text = "Please input username",font=font_stylize).grid(column = 1,row = 3)
get_name = tk.Entry(root).grid(column=3,row=3)

surname = tk.Label(root, text = "Please input password",font=font_stylize).grid(column=1,row=4)
get_surname = tk.Entry(root).grid(column=3,row=4)



#the button
play = tk.Button(root,text = "Login",font=font_stylize,bg="coral").grid(column=2,row=12)
register_user = tk.Button(root, text ="Register New User", font=font_stylize, bg="coral").grid(column=3, row=12)

#starting the form
root.mainloop()
