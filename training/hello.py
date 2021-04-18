# First we imported the Flask class.
# An instance of this class will be our WSGI application.
from flask import Flask

# Next we create an instance of this class.
# The first argument is the name of the application’s module or package.
# If you are using a single module (as in this example),
# you should use __name__
# because depending on if it’s started as application or
# imported as module the name will be different ('__main__' versus the actual import name).
app = Flask(__name__)

# We then use the route() decorator to tell Flask what URL should trigger our function.
# The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.


@app.route('/')
def hello_world():
    return 'Hello, World!'
