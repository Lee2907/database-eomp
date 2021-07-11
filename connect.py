import mysql.connector
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='lifechoicesonline')
mycursor=mydb.cursor()
xy=mycursor.execute('Select * from lifechoicesonline')
for i in mycursor:
    print(i)
