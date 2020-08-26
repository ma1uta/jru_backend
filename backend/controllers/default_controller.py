import connexion
import six

from backend.models.articles_response import ArticlesResponse  # noqa: E501
from backend.models.auth import Auth  # noqa: E501
from backend.models.domain_list import DomainList  # noqa: E501
from backend.models.error_result import ErrorResult  # noqa: E501
from backend.models.feedback import Feedback  # noqa: E501
from backend.models.mam_message_list_response import MAMMessageListResponse  # noqa: E501
from backend.models.mam_message_request import MAMMessageRequest  # noqa: E501
from backend.models.mam_settings import MAMSettings  # noqa: E501
from backend.models.mam_settings_response import MAMSettingsResponse  # noqa: E501
from backend.models.register import Register  # noqa: E501
from backend.models.roster_list_response import RosterListResponse  # noqa: E501
from backend.models.v_card_response import VCardResponse  # noqa: E501
from backend import util
from backend.__main__ import db


def get_articles():  # noqa: E501
    """get articles

    news! # noqa: E501


    :rtype: ArticlesResponse
    """

    return 'do some magic!'


def get_domains():  # noqa: E501
    """get domains

    domains... # noqa: E501


    :rtype: DomainList
    """
    return 'do some magic!'


def get_logout():  # noqa: E501
    """logout

    invalidate credentials # noqa: E501


    :rtype: ErrorResult
    """
    return 'do some magic!'


def get_roster():  # noqa: E501
    """get the roster

    retrieve user roster # noqa: E501


    :rtype: RosterListResponse
    """
    return 'do some magic!'


def get_settings():  # noqa: E501
    """get MAM settings

    get MAM settings # noqa: E501


    :rtype: MAMSettingsResponse
    """
    return 'do some magic!'


def get_vcard():  # noqa: E501
    """get user vcard

    get user vcard # noqa: E501


    :rtype: VCardResponse
    """
    return 'do some magic!'


def post_feedback(body):  # noqa: E501
    """sent a feedback

    sent a message to site admins # noqa: E501

    :param body: request body
    :type body: dict | bytes

    :rtype: ErrorResult
    """
    if connexion.request.is_json:
        body = Feedback.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_login(body):  # noqa: E501
    """login

    login # noqa: E501

    :param body: user credentials
    :type body: dict | bytes

    :rtype: ErrorResult
    """
    if connexion.request.is_json:
        body = Auth.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_messages(body):  # noqa: E501
    """get mam messages

    get mam messages from the specified jid # noqa: E501

    :param body: message owner
    :type body: dict | bytes

    :rtype: MAMMessageListResponse
    """
    if connexion.request.is_json:
        body = MAMMessageRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_register(body):  # noqa: E501
    """register

    register a new account # noqa: E501

    :param body: register data
    :type body: dict | bytes

    :rtype: ErrorResult
    """
    if connexion.request.is_json:
        body = Register.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_reset(body):  # noqa: E501
    """reset password

    sent an email message with the link to reset password # noqa: E501

    :param body: reset request body
    :type body: dict | bytes

    :rtype: ErrorResult
    """
    if connexion.request.is_json:
        body = Register.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_setemail(body):  # noqa: E501
    """set an email

    link jid with the email # noqa: E501

    :param body: set email request body
    :type body: dict | bytes

    :rtype: ErrorResult
    """
    if connexion.request.is_json:
        body = Register.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_settings(body):  # noqa: E501
    """set MAM settings

    set MAM settings # noqa: E501

    :param body: request body
    :type body: dict | bytes

    :rtype: ErrorResult
    """
    if connexion.request.is_json:
        body = MAMSettings.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
