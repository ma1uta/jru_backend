import json

import urllib3

from ..config import config
from ..dto.common import ERR_CAPTCHA_FAILED

http = urllib3.PoolManager


def check_recaptcha(captcha, ip):
    resp = http.request(
        method="POST",
        url="https://www.google.com/recaptcha/api/siteverify",
        fields={
            "secret": config().recaptcha_secret,
            "response": captcha,
            "remoteip": ip
        }
    )
    resp_data = json.load(resp.data.decode("utf-8"))
    if not resp_data.success:
        return ERR_CAPTCHA_FAILED

    return None
