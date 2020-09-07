from ..dto.common import ERR_INCOMPLETE_DATA
from .common import ok, error, is_valid_jid
from .disposable_email import is_disposable_email
from .recaptcha import check_recaptcha

from datetime import datetime, timedelta


def register(data, ip):
    """Registration"""
    if data.hash and data.password:
        return register_flow(data, ip)

    if not (not data.captcha and data.login and (data.email or data.phone)):
        return error(ERR_INCOMPLETE_DATA)
    captcha_error = check_recaptcha(data.captcha, ip)
    if captcha_error:
        return error(captcha_error)

    jid_validation_error = is_valid_jid(data.login)
    if not jid_validation_error:
        return jid_validation_error

    email_error = is_disposable_email(data.email.lower())
    if email_error:
        return error(email_error)

    expires = datetime.today() + timedelta(days=1)
    token = login(data.login, expires)
    url = ""
    email_data = EmailData(
        email=data.email,
        token=token,
        username=data.login,
        link=url
    )
    send_email("register", email_data)

    return ok()


def register_flow(data, ip):
    if not data.hash or not data.password:
        return error(ERR_INCOMPLETE_DATA)

    register_user(data.login, data.password, data.email, ip)
    return ok()


def register_user(username, password, email, ip):
    pass


def login(username, expires):
    return Token(token="", error_msg=None)


def send_email(kind, data):
    pass


class Token:
    token = None
    error = None

    def __init__(self, token, error_msg):
        self.token = token
        self.error = error_msg


class EmailData:
    to = None
    login = None
    subject = None
    link = None

    def __init__(self, email, username, subject, link):
        self.to = email
        self.login = email
        self.subject = subject
        self.link = link


