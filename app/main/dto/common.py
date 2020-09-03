from flask_restplus import Namespace, fields


class CommonDto:
    api = Namespace('common')
    result = api.model('result', {
        'result': fields.String,
        'error': fields.String
    })


ERR_INVALID_CONTENT_TYPE = "invalid-content-type"
ERR_NOT_AUTHORIZED = "not-authorized"
ERR_BAD_JSON = "bad-json"
ERR_SERVICE_ERROR = "service-error"
ERR_INCOMPLETE_DATA = "incomplete-data"
ERR_CAPTCHA_FAILED = "captcha-failure"
ERR_LOGIN_ALREADY_EXISTS = "login-already-exists"
ERR_INVALID_EMAIL = "invalid-email"
ERR_INVALID_JID = "invalid-jid"
ERR_NOT_FOUND = "not-found"
ERR_ONE_TIME_EMAIL = "one-time-email"
ERR_UNKNOWN_MAIL_DOMAIN = "unknown-mail-domain"
ERR_EMAIL_NOT_EXISTS = "email-not-exists"
ERR_EMAIL_EXCEEDS = "email-exceeds"
ERR_WEAK_PASSWORD = "weak-password"
