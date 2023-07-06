# python code(server)
# Flask framework - lightweight python framework for creating webapplications
# import flask 
from flask import Flask
# create the main app
app=Flask(__name__)
# routing -creating flask routes/pages
# main route
@app.route("/")
# every route must have a function
def main():
    return "This is the main route"


# second route
@app.route("/about")
def About():
    return "This is the About route"
@app.route("/services")
def services():
    date="5/7/2023"
    print(date)
    return f"today's date is {date}"
# create a route that returns a list of great revolutions in the world
@app.route("/revolutions")
def revolutions():
    revolutions=['American Revolt','History revolt']
    return f"{revolutions}"











app.run(debug=True)
              