from flask import Flask, request
from flask_restful import Resource, Api
from model import make_sentence


app = Flask(__name__)
api = Api(app)

todo = {}

class TodoSimple(Resource):
    def get(self, route_id):
        todo[route_id] = request.form['data']
        return {route_id: make_sentence(todo[route_id])}

api.add_resource(TodoSimple, '/<string:route_id>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
