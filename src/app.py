from flask import Flask, request, render_template
from flask_restful import Resource, Api
import random as r

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return render_template("index.html") 

api.add_resource(Home, '/')


class Add(Resource):
    def get(self):
        num1 = request.args.get('num1')
        print(type(num1))
        num2 = request.args.get('num2')
        print(type(num2))
        return f"Sum is {int(num1) + int(num2)}"

api.add_resource(Add, '/add')

class Substract(Resource):
    def get(self):
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
        return f"Substract is {int(num1) - int(num2)}"

api.add_resource(Substract, '/substract')


class Division(Resource):
    def get(self):
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
        return f"Division is {float(num1) / float(num2)}"

api.add_resource(Division, '/division')

class Random(Resource):
    def get(self):
        i = 0
        num1 = request.args.get('num1')
        if num1 == None:
            count = 10
        else:
            count = int(num1)
        s = " "
        array = []
        while i < count:
            array.append(str(r.randint(0, 9)))
            i += 1
        return f'{str(count)} random numbers: {s.join(array)}'

api.add_resource(Random, '/random')

class Readiness(Resource):
    def get(self):
        return "200 - Readiness"

api.add_resource(Readiness, '/readiness')

class Liveness(Resource):
    def get(self):
        return "200 - Liveness"

api.add_resource(Liveness, '/liveness')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

