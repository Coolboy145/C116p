# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Bartosz" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
def father():
    name = "Plech"
    age = "50"

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
def mother():
    name = "Dorota"
    age = "50"

    return render_template('index.html', name = name, age = age)

# define the route to friends webpage
def friends():
    name = "Bobek"
    age = "14"

    return render_template('index.html', name = name, age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
