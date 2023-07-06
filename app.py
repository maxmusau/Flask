# python code(server)
# Flask framework - lightweight python framework for creating webapplications
# import flask 
from flask import Flask,render_template,request
import pymysql
import mysql.connector
# create the main app
app=Flask(__name__)
# temporary memory to store records
users=[]

# routing -creating flask routes/pages
# main route
@app.route("/")
# every route must have a function
def main():
    #TODO
    # pass
    return render_template("index.html")
@app.route("/register",methods=['POST','GET'])
# CRUD Create(POST), Read(GET),Update(PUT),Delete(DELETE)
def register():
    # check whether or not the user has posted some data
    if request.method == 'POST':
        #TODO
        username=request.form['username']
        email=request.form.get('email')
        password=request.form.get('password')
        confirm=request.form.get('confirm_password')
        # input validation
        # check if all the fields have data
        if not username or not email or not password or not confirm:
            return render_template("signup.html",message="Error: Please fill in all the fields")
        # check if password matches confirm password
        elif password != confirm:
            return render_template("signup.html",message="Error: Passwords do not match")
        # check if users exists
        for user in users:
            if user["username"]==username:
                return render_template("signup.html",message="Error: User already exists")
            # create an object to hold the user details 
        user= {
            "username":username,
            "email":email,
            "password":password
        }  
        # append the new user to the list
        users.append(user)
        return '<h2>Registration Successful</h2> \n' '<a href="/register" style="color:blue">Go Back</a>'
    else:
        return render_template("signup.html")
    
@app.route('/users')
def display_users():
    # print(users)
    for user in users:
        print(f"Username: {user['username']}")
    return users

# route to save employees
@app.route("/save_employee",methods=['POST','GET'])
def save_employees():
    # check if any records have been posted
    if request.method=='POST':
        #TODO
        # define the connection 
        connection=pymysql.connect(host="localhost",user="root",password="",database="maxwell")
        # get data from the form
        name=request.form['name']
        email=request.form['email']
        course=request.form['course']
        university=request.form['university']
        # university=request.form.get("university")

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
        return render_template("employees.html",response="Employee Saved Successfuly")
        
    else:
        return render_template("employees.html",message="Enter records to save employee")




app.run(debug=True)
              