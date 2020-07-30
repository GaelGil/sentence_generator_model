from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from model import make_sentence


app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('sentence')


class callSentenceGenerator(Resource):
    def post(self):
        """
        Send the data to the model
        """
        args = parser.parse_args()
        return make_sentence(args['sentence'])

##
## Actually setup the Api resource routing here
##
api.add_resource(callSentenceGenerator, '/sentence')
# api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True) 