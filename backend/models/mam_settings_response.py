# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from backend.models.base_model_ import Model
from backend.models.error_result import ErrorResult  # noqa: F401,E501
from backend.models.mam_settings import MAMSettings  # noqa: F401,E501
from backend import util


class MAMSettingsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, default: str=None, always: List[str]=None, never: List[str]=None, created_at: datetime=None, result: str=None, error: str=None):  # noqa: E501
        """MAMSettingsResponse - a model defined in Swagger

        :param default: The default of this MAMSettingsResponse.  # noqa: E501
        :type default: str
        :param always: The always of this MAMSettingsResponse.  # noqa: E501
        :type always: List[str]
        :param never: The never of this MAMSettingsResponse.  # noqa: E501
        :type never: List[str]
        :param created_at: The created_at of this MAMSettingsResponse.  # noqa: E501
        :type created_at: datetime
        :param result: The result of this MAMSettingsResponse.  # noqa: E501
        :type result: str
        :param error: The error of this MAMSettingsResponse.  # noqa: E501
        :type error: str
        """
        self.swagger_types = {
            'default': str,
            'always': List[str],
            'never': List[str],
            'created_at': datetime,
            'result': str,
            'error': str
        }

        self.attribute_map = {
            'default': 'default',
            'always': 'always',
            'never': 'never',
            'created_at': 'created_at',
            'result': 'result',
            'error': 'error'
        }
        self._default = default
        self._always = always
        self._never = never
        self._created_at = created_at
        self._result = result
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'MAMSettingsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MAMSettingsResponse of this MAMSettingsResponse.  # noqa: E501
        :rtype: MAMSettingsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def default(self) -> str:
        """Gets the default of this MAMSettingsResponse.


        :return: The default of this MAMSettingsResponse.
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default: str):
        """Sets the default of this MAMSettingsResponse.


        :param default: The default of this MAMSettingsResponse.
        :type default: str
        """

        self._default = default

    @property
    def always(self) -> List[str]:
        """Gets the always of this MAMSettingsResponse.


        :return: The always of this MAMSettingsResponse.
        :rtype: List[str]
        """
        return self._always

    @always.setter
    def always(self, always: List[str]):
        """Sets the always of this MAMSettingsResponse.


        :param always: The always of this MAMSettingsResponse.
        :type always: List[str]
        """

        self._always = always

    @property
    def never(self) -> List[str]:
        """Gets the never of this MAMSettingsResponse.


        :return: The never of this MAMSettingsResponse.
        :rtype: List[str]
        """
        return self._never

    @never.setter
    def never(self, never: List[str]):
        """Sets the never of this MAMSettingsResponse.


        :param never: The never of this MAMSettingsResponse.
        :type never: List[str]
        """

        self._never = never

    @property
    def created_at(self) -> datetime:
        """Gets the created_at of this MAMSettingsResponse.


        :return: The created_at of this MAMSettingsResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """Sets the created_at of this MAMSettingsResponse.


        :param created_at: The created_at of this MAMSettingsResponse.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def result(self) -> str:
        """Gets the result of this MAMSettingsResponse.


        :return: The result of this MAMSettingsResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result: str):
        """Sets the result of this MAMSettingsResponse.


        :param result: The result of this MAMSettingsResponse.
        :type result: str
        """

        self._result = result

    @property
    def error(self) -> str:
        """Gets the error of this MAMSettingsResponse.


        :return: The error of this MAMSettingsResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error: str):
        """Sets the error of this MAMSettingsResponse.


        :param error: The error of this MAMSettingsResponse.
        :type error: str
        """

        self._error = error