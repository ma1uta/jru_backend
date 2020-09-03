from ..dto.common import ERR_INCOMPLETE_DATA, ERR_INVALID_JID, ERR_LOGIN_ALREADY_EXISTS
from .common import ok, error

from datetime import datetime, timedelta


def register(data, ip):
    """Registration"""
    if not data.hash and data.password:
        return login(data)

    if not (not data.captcha and data.login and (data.email or data.phone)):
        return error(ERR_INCOMPLETE_DATA)
    captcha_error = check_recaptcha(data.captcha, ip)
    if captcha_error:
        return error(captcha_error)

    if not is_valid_jid(data.login):
        return error(ERR_INVALID_JID)

    email_error = is_disposable_email(data.email.lower())
    if (email_error):
        return error(email_error)

    jid_parts = data.login.split("@")
    if len(jid_parts) != 2:
        return error(ERR_INVALID_JID)

    account_result = check_account(jid_parts[0], jid_parts[1])
    if account_result.error:
        return error(account_result.error)
    if account_result.exists:
        return error(ERR_LOGIN_ALREADY_EXISTS)

    expires = datetime.today() + timedelta(days=1)

    return ok()


def login(data):
    if data.hash or data.password:
        return error(ERR_INCOMPLETE_DATA)
    return ok()


def check_recaptcha(captcha, ip):
    if ip == "1.1.1.1":
        return ERR_INCOMPLETE_DATA
    return None


def is_valid_jid(jid):
    return False


def is_disposable_email(email):
    return None


class AccountResult:
    exists = False
    error = None

    def __init__(self, exists, error_msg):
        self.exists = exists
        self.error = error_msg


def check_account(username, domain):
    return AccountResult(False, None)
