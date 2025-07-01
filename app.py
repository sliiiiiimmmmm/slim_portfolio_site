from flask import Flask

# Create app object of Flask class
app = Flask(__name__)

# This is the route for the default URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

# This will run the app on port 8080
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)