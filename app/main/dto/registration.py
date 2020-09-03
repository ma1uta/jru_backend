from flask_restplus import Namespace, fields


class RegistrationDto:
    api = Namespace('register_start')
    register = api.model('register', {
        'captcha': fields.String,
        'login': fields.String,
        'password': fields.String,
        'email': fields.String,
        'phone': fields.String,
        'hash': fields.String
    })

