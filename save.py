# save to the database
import pymysql
import mysql.connector
# define the connection 
connection=pymysql.connect(host="localhost",user="root",password="",database="maxwell")
# define the columns to save
name="Eunice Njeri"
email="eunice@gmail.com"
course="Sports"
university="Egerton University"

# values=(30498,3,"Headphones","Nakuru")

# define the sql query
sql='insert into employees(name,email,course,university) values(%s,%s,%s,%s)'
# sql_orders='insert into orders(order_id,user_id,order_name,destination) values(%s,%s,%s,%s)'
# create cursor - used to execute the sql query
cursor=connection.cursor() #function
# execute sql
cursor.execute(sql,(name,email,course,university))
# cursor.execute(sql_orders,values)

# commit the changes to the database
connection.commit()
print("saved successfuly")
# close the cursor
cursor.close()
