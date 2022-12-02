from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # We can insert some HTML here! Try to make the text here bold using the <b> tag
    return 'Web App with Python Flask!', 200, {"Content-type":"text/html"}


app.run(host='0.0.0.0', port=8000)
