import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="root")

con=conn.cursor()
con.execute("show databases")
for i in con:
    print(i)