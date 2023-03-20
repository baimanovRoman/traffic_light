from flask import Flask
from flask_restx import Api


app = Flask(__name__)
app.config["RESTX_VALIDATE"] = True


from resources.traffic_light import api as ApiSetCommandTrafficLight


api = Api(app, prefix="/api/v1", version="1.0", title="Traffic light", description="Api traffic light")
api.add_namespace(ApiSetCommandTrafficLight)
