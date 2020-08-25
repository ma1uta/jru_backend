# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from backend.models.base_model_ import Model
from backend.models.error_result import ErrorResult  # noqa: F401,E501
from backend.models.roster import Roster  # noqa: F401,E501
from backend.models.roster_list import RosterList  # noqa: F401,E501
from backend import util


class RosterListResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, roster: List[Roster]=None, result: str=None, error: str=None):  # noqa: E501
        """RosterListResponse - a model defined in Swagger

        :param roster: The roster of this RosterListResponse.  # noqa: E501
        :type roster: List[Roster]
        :param result: The result of this RosterListResponse.  # noqa: E501
        :type result: str
        :param error: The error of this RosterListResponse.  # noqa: E501
        :type error: str
        """
        self.swagger_types = {
            'roster': List[Roster],
            'result': str,
            'error': str
        }

        self.attribute_map = {
            'roster': 'roster',
            'result': 'result',
            'error': 'error'
        }
        self._roster = roster
        self._result = result
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'RosterListResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RosterListResponse of this RosterListResponse.  # noqa: E501
        :rtype: RosterListResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def roster(self) -> List[Roster]:
        """Gets the roster of this RosterListResponse.


        :return: The roster of this RosterListResponse.
        :rtype: List[Roster]
        """
        return self._roster

    @roster.setter
    def roster(self, roster: List[Roster]):
        """Sets the roster of this RosterListResponse.


        :param roster: The roster of this RosterListResponse.
        :type roster: List[Roster]
        """

        self._roster = roster

    @property
    def result(self) -> str:
        """Gets the result of this RosterListResponse.


        :return: The result of this RosterListResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result: str):
        """Sets the result of this RosterListResponse.


        :param result: The result of this RosterListResponse.
        :type result: str
        """

        self._result = result

    @property
    def error(self) -> str:
        """Gets the error of this RosterListResponse.


        :return: The error of this RosterListResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error: str):
        """Sets the error of this RosterListResponse.


        :param error: The error of this RosterListResponse.
        :type error: str
        """

        self._error = error