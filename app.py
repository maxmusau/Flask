# python code(server)
# Flask framework - lightweight python framework for creating webapplications
# import flask 
from flask import *
import pymysql
import mysql.connector
# create the main app
app=Flask(__name__)
# temporary memory to store records
users=[]
connection=pymysql.connect(host="localhost",user="root",password="",database="maxwell")
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
        password=request.form['password']
        course=request.form['course']
        university=request.form['university']
        # university=request.form.get("university")
        # check if image has been uploaded
        if 'image' not in request.files:
            return render_template("employees.html",message="Image not uploaded")
       
        image=request.files['image']
        # store the image inside static folder
        image.save('static/images/'+image.filename)
        img_name=image.filename
        # Input validation
        if not name or not email or not course or not university:
            return render_template("employees.html",message="Please fill in all the records")
        # check if username has two words
        if " " not in name:
            return render_template("employees.html",message="name must be two words")
        # check if employee exists
        sql ='select * from employees where email=%s'
        cursor=connection.cursor() 
        cursor.execute(sql,email)  
        if cursor.rowcount==1:
            return render_template("employees.html",message="User already exists. Use a different email address or login")
        else:  
            # values=(30498,3,"Headphones","Nakuru")
            connection=pymysql.connect(host="localhost",user="root",password="",database="maxwell")
            # define the sql query
            sql='insert into employees(name,email,password,course,university,img_name) values(%s,%s,%s,%s,%s,%s)'
            # create cursor - used to execute the sql query
            cursor=connection.cursor() #function
            # execute sql
            cursor.execute(sql,(name,email,password,course,university,img_name))
            # commit the changes to the database
            connection.commit()
            # close the cursor
            cursor.close()
            return render_template("employees.html",response="Employee Saved Successfuly")
            
    else:
        return render_template("employees.html",message="Enter records to save employee")




# CRUD
# Retrieve/fetch records from the database
@app.route("/get_employees",methods=['POST','GET'])
def Get_employee():
    #already defined connection, variable is connection
    
    # define the sql query-select
    sql = 'select * from employees'
    # create cursor function to execute sql query
    cursor=connection.cursor()
    # execute the sql query
    cursor.execute(sql)
    # check if there are records in the database
    if cursor.rowcount==0: 
        response='No records to display'
        return render_template("get_employees.html",message=response)
    else:
    #    fetch all the records 
        employees=cursor.fetchall()
        return render_template("get_employees.html",data=employees)
        # represent the data using a table
        
    # API
# update route
@app.route("/edit",methods=['POST','GET'])
def Edit():
    # check if data has been posted
    if request.method=='POST':
        # get the posted data
        user_id=request.form.get("user_id")
        Email=request.form.get("email")
        # connection defined
        # create the cursor function
        edit_cursor=connection.cursor()
        sql='update employees set email=%s where user_id=%s'
        
        sql_check='select user_id from employees where user_id=%s'
        check_cursor=connection.cursor()
        check_cursor.execute(sql_check,userid)
        record=check_cursor.fetchone()
        # chek if user id exists
        if check_cursor.rowcount ==0:
            return render_template("edit.html",message="User_id does not exist")
        else:
            # execute the sql query
            edit_cursor.execute(sql,(Email,user_id))
            # commit the changes
            connection.commit()
            return render_template("edit.html",message="Email updated successfully")
    else:
        return render_template("edit.html")
    
    
    












app.run(debug=True)
              