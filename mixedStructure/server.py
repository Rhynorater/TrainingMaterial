from flask import Flask,request
import datetime

app = Flask(__name__)
names = {}

@app.route('/checkUser')
def index():
    if request.args['name'] in names:
        time = names[request.args['name']]
        return '{"name":"'+request.args['name']+'", "time":"'+time+'", "alreadyRegistered":true, "registered":false}', 200, {"Content-Type":"text/html", "Access-Control-Allow-Origin":"*"}
    else:
        names[request.args['name']]=str(datetime.datetime.now())
        return '{"name":"'+request.args['name']+'", "alreadyRegistered":false, "registered":true}', 200, {"Content-Type":"text/html", "Access-Control-Allow-Origin":"*"}


app.run(host='0.0.0.0', port=8001)
