from flask import Flask
from flask_restplus import Api, Resource, fields


app = Flask(__name__)
api = Api(
    app=app,
    version="1.0",
    title="Covid19-VA",
    description="An API for Covid19-VA data.",
)

name_space = api.namespace("main", description="Main APIs")


@name_space.route("/")
class MainClass(Resource):
    def get(self):
        return {"status": "Got new data"}

    def post(self):
        return {"status": "Posted new data"}


if __name__ == "__main__":
    app.run(debug=True)
