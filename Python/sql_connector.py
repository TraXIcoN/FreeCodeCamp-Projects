import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="pourush")
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("create database happy") 
mycursor.execute("show databases")
for i in mycursor:
    print(i)
