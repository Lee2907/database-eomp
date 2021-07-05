import tkinter as tk

# initializing tkinter
root = tk.Tk()
root.title("The Log Connect")
root.geometry("775x426")
root.config(bg="peach puff")

font_stylize = ("Verdana",11)

name = tk.Label(root, text = "Please enter name:",font=font_stylize).grid(column = 1,row = 3)
get_name = tk.Entry(root).grid(column=3,row=3)

surname = tk.Label(root, text = "Please enter surname:",font=font_stylize).grid(column=1,row=4)
get_surname = tk.Entry(root).grid(column=3,row=4)

id_no = tk.Label(root, text = "ID No: ",font=font_stylize).grid(column = 1,row = 3)
get_id = tk.Entry(root).grid(column=3,row=3)

phone_no = tk.Label(root, text = "Phone No:",font=font_stylize).grid(column = 1,row = 3)
get_phone = tk.Entry(root).grid(column=3,row=3)

nextofkin_name = tk.Label(root, text = "Next of Kin's Name:",font=font_stylize).grid(column=1,row=4)
get_nokn = tk.Entry(root).grid(column=3,row=4)

nextofkin_no = tk.Label(root, text = "Next of Kin's Phone No: ",font=font_stylize).grid(column = 1,row = 3)
get_nokn2 = tk.Entry(root).grid(column=3,row=3)

root.mainloop()
