from flask import Flask, request, render_template
from flask_restful import Resource, Api
import random as r

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return render_template("index.html") 

api.add_resource(Home, '/')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0')

