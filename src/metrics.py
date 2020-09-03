from flask import Flask, request, render_template, redirect
from flask_restful import Resource, Api
import random as r

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return render_template("index.html") 

api.add_resource(Home, '/')


class Metrics(Resource):
    def get(self):
        url = "http://3.84.185.73:30000"
        return redirect(url, code=302)

api.add_resource(Metrics, '/metrics')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

