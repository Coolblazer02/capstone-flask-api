from flask import Flask

# create a flask app instance
app = Flask(__name__)

# define a route and a view function
@app.route('/')
def hello():
    return 'hello, world!'

# run the app
if __name__ == '__main__':
    app.run(debug=True)