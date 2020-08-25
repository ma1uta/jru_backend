# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from backend.models.base_model_ import Model
from backend.models.article import Article  # noqa: F401,E501
from backend.models.articles import Articles  # noqa: F401,E501
from backend.models.error_result import ErrorResult  # noqa: F401,E501
from backend import util


class ArticlesResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, articles: List[Article]=None, result: str=None, error: str=None):  # noqa: E501
        """ArticlesResponse - a model defined in Swagger

        :param articles: The articles of this ArticlesResponse.  # noqa: E501
        :type articles: List[Article]
        :param result: The result of this ArticlesResponse.  # noqa: E501
        :type result: str
        :param error: The error of this ArticlesResponse.  # noqa: E501
        :type error: str
        """
        self.swagger_types = {
            'articles': List[Article],
            'result': str,
            'error': str
        }

        self.attribute_map = {
            'articles': 'articles',
            'result': 'result',
            'error': 'error'
        }
        self._articles = articles
        self._result = result
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'ArticlesResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ArticlesResponse of this ArticlesResponse.  # noqa: E501
        :rtype: ArticlesResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def articles(self) -> List[Article]:
        """Gets the articles of this ArticlesResponse.


        :return: The articles of this ArticlesResponse.
        :rtype: List[Article]
        """
        return self._articles

    @articles.setter
    def articles(self, articles: List[Article]):
        """Sets the articles of this ArticlesResponse.


        :param articles: The articles of this ArticlesResponse.
        :type articles: List[Article]
        """

        self._articles = articles

    @property
    def result(self) -> str:
        """Gets the result of this ArticlesResponse.


        :return: The result of this ArticlesResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result: str):
        """Sets the result of this ArticlesResponse.


        :param result: The result of this ArticlesResponse.
        :type result: str
        """

        self._result = result

    @property
    def error(self) -> str:
        """Gets the error of this ArticlesResponse.


        :return: The error of this ArticlesResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error: str):
        """Sets the error of this ArticlesResponse.


        :param error: The error of this ArticlesResponse.
        :type error: str
        """

        self._error = error