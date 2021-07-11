from tkinter import *
import mysql.connector

root = Tk()
root.title("The Log Connect")
root.geometry("500x500")
root.config(bg="peach puff")

font_style = ("Palatino",14)


#establishing the connection
conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='mydb')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
   # Executing the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

# Closing the connection
conn.close()

username = Label(root, text = "Username",font=font_style).grid(column = 1,row = 9)
get_name = Entry(root).grid(column=3,row=9)

password = Label(root, text = "Password",font=font_style).grid(column=1,row=10)
get_pass = Entry(root).grid(column=3,row=10)

password2 = Label(root, text = "Confirm Password",font=font_style).grid(column=1,row=11)
get_pass2 = Entry(root).grid(column=3,row=11)

register_user = Button(root, text ="Log In", font=font_style, bg="light steel blue").grid(column=2, row=14)

root.mainloop()
