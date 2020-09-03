from flask_restplus import Resource
from flask import request
from ..dto.registration import RegistrationDto
from ..dto.common import CommonDto
from ..service.registration import register

api = RegistrationDto.api
_register = RegistrationDto.register
_common = CommonDto.result


@api.route("/json/register")
class Registration(Resource):
    @api.doc("Start registration")
    @api.expect(_register, validate=True)
    @api.marshal_with(_common)
    def get(self):
        """ Start registration """
        dto = request.json
        return register(dto, request.remote_addr)
