from flask_restx import  Namespace, Resource, fields, reqparse
from flask import request, Response
from services.command_factory import CommandFactory

api = Namespace('Command traffic light', description="Set Command traffic light", path='/')


class TrafficLightResponseDto:
    set_command = api.model("set_command_response_dto", {
        'command': fields.String(required=True, description="Command for traffic light"),
        'metadata': fields.Raw(required=False, description="Metadata for traffic light")
    })


@api.route('/', methods=['POST'])
class SetCommandTrafficLight(Resource):
    @api.expect(TrafficLightResponseDto.set_command)
    def post(self):
        command = api.payload.get('command')
        metadata = api.payload.get('metadata')
        command_factory = CommandFactory()
        command_class = command_factory.create_command(command)
        command_class.set_metadata(metadata)
        result = command_class.get_result()
        if result is not None:
            return Response(result)
        return 200


