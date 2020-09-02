from flask import Flask, request, render_template
from flask_restful import Resource, Api
import random as r

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return render_template("index.html") 

api.add_resource(Home, '/')

class Division(Resource):
    def get(self):
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
        return f"Division is {float(num1) / float(num2)}"

api.add_resource(Division, '/division')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

