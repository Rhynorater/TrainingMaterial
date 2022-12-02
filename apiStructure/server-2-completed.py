from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!', 200, {"Content-type":"text/html"}

## Add a function here that defines the route "greenting" and greets the user by name
@app.route('/greeting')
def greeting():
    return "Hello" + request.args.get('name')

app.run(host='0.0.0.0', port=8000)
