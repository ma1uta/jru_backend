from ..config import config
from ..dto.common import ERR_INVALID_JID, ERR_LOGIN_ALREADY_EXISTS


def error(msg):
    return {
        "error": msg
    }


def ok():
    return {
        "result": "ok"
    }


def is_valid_jid(jid):
    parts = jid.split("@")
    if len(parts) != 2:
        return error(ERR_INVALID_JID)

    valid_domain = False
    for domain in config().domains:
        if domain == parts[1]:
            valid_domain = True

    if not valid_domain:
        return error(ERR_INVALID_JID)
    account_result = check_account(parts[0], parts[1])
    if account_result.error:
        return error(account_result.error)
    if account_result.exists:
        return error(ERR_LOGIN_ALREADY_EXISTS)

    return None


class AccountResult:
    exists = False
    error = None

    def __init__(self, exists, error_msg):
        self.exists = exists
        self.error = error_msg


def check_account(username, domain):
    return AccountResult(False, None)
