import flask
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


class Request(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("text")
        params = parser.parse_args()
        with open("texts", "a") as f:
            f.write(params.text + "\n")
        return {}, 201


@app.route('/')
def show():
    with open("texts", "r") as f:
        return f.read()


api.add_resource(Request, "/text")
if __name__ == '__main__':
    app.run()