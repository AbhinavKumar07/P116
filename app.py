# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    my_name = "Abhinav Kumar" 
    my_age = "15" 

    return render_template('index.html' , name = my_name , age = my_age)

# define the route to father webpage
@app.route('/dad')

def dad():
    dad_name =  "Raj Kumar"
    dad_age = "4_"

    return  render_template('father.html' , name = dad_name , age = dad_age)

# define the route to mother webpage

@app.route('/mom')

def mom():
    mom_name = "Mom"
    mom_age = "4_"

    return render_template("mother.html" , name  = mom_name , age = mom_age)


# define the route to friends webpage

@app.route('/friend1')

def friend1():
    friend1_name = "Friend1"
    friend1_age = 15

    return render_template("friend.html" , name = friend1_name , age = friend1_age)
    
@app.route('/friend2')
def friend2():
    friend2_name = "Friend2"
    friend2_age = 16

    return render_template("friend.html" , name = friend2_name , age = friend2_age)


# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
