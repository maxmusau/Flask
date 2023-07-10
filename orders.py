from flask import *
import pymysql #or mysql_connector
# create app
app=Flask(__name__)
# create orders route
@app.route("/",methods=['POST','GET']) #HTTP response methods
def orders():
    #TODO
    # CRUD 
    # create- POST
    # read-GET
    # update-PUT
    #delete-DELETE
    # check if user has posted any data
    if request.method =='POST':
        # TODO
        # get data from the form
        order_id=request.form.get("order_id")
        user_id=request.form.get("user_id")
        order_name=request.form.get("order_name")
        destination=request.form.get("destination")
        
        # input validation
        # check if all the fields have data
        if not order_id or not user_id or not order_name or not destination:
            return render_template("orders.html",error="You must fill in all the fields")
        # check if order id is 4 digits
        elif len(order_id) !=4:
            return render_template("orders.html",error="Order id must have 4 digits")
        # check if name has two words
        elif " " not in order_name:
            return render_template("orders.html",error="you must provide two names")
        else:
            connection=pymysql.connect(host="localhost",user="root",password="",database="maxwell")
            # define the sql query
            sql='insert into orders(order_id,user_id,order_name,destination) values(%s,%s,%s,%s)'
            
            # create cursor - used to execute the sql query
            cursor=connection.cursor() #function
            # execute sql
            cursor.execute(sql,(order_id,user_id,order_name,destination))
            # cursor.execute(sql_orders,values)

            # commit the changes to the database
            connection.commit()
            print("saved successfuly")
            # close the cursor
            cursor.close()
            return render_template("orders.html",message="order Saved Successfuly")
            

    else:
        return render_template("orders.html",message="Enter records to save order")
                    
                    
                    
               

# run app
app.run(debug=True,port=8000) #
