# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from backend.models.base_model_ import Model
from backend import util


class Article(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, author: str=None, title: str=None, body: str=None, posted: datetime=None, modified: datetime=None, published: datetime=None, tags: List[str]=None, alias: str=None):  # noqa: E501
        """Article - a model defined in Swagger

        :param id: The id of this Article.  # noqa: E501
        :type id: str
        :param author: The author of this Article.  # noqa: E501
        :type author: str
        :param title: The title of this Article.  # noqa: E501
        :type title: str
        :param body: The body of this Article.  # noqa: E501
        :type body: str
        :param posted: The posted of this Article.  # noqa: E501
        :type posted: datetime
        :param modified: The modified of this Article.  # noqa: E501
        :type modified: datetime
        :param published: The published of this Article.  # noqa: E501
        :type published: datetime
        :param tags: The tags of this Article.  # noqa: E501
        :type tags: List[str]
        :param alias: The alias of this Article.  # noqa: E501
        :type alias: str
        """
        self.swagger_types = {
            'id': str,
            'author': str,
            'title': str,
            'body': str,
            'posted': datetime,
            'modified': datetime,
            'published': datetime,
            'tags': List[str],
            'alias': str
        }

        self.attribute_map = {
            'id': 'id',
            'author': 'author',
            'title': 'title',
            'body': 'body',
            'posted': 'posted',
            'modified': 'modified',
            'published': 'published',
            'tags': 'tags',
            'alias': 'alias'
        }
        self._id = id
        self._author = author
        self._title = title
        self._body = body
        self._posted = posted
        self._modified = modified
        self._published = published
        self._tags = tags
        self._alias = alias

    @classmethod
    def from_dict(cls, dikt) -> 'Article':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Article of this Article.  # noqa: E501
        :rtype: Article
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Article.


        :return: The id of this Article.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Article.


        :param id: The id of this Article.
        :type id: str
        """

        self._id = id

    @property
    def author(self) -> str:
        """Gets the author of this Article.


        :return: The author of this Article.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author: str):
        """Sets the author of this Article.


        :param author: The author of this Article.
        :type author: str
        """

        self._author = author

    @property
    def title(self) -> str:
        """Gets the title of this Article.


        :return: The title of this Article.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Article.


        :param title: The title of this Article.
        :type title: str
        """

        self._title = title

    @property
    def body(self) -> str:
        """Gets the body of this Article.


        :return: The body of this Article.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body: str):
        """Sets the body of this Article.


        :param body: The body of this Article.
        :type body: str
        """

        self._body = body

    @property
    def posted(self) -> datetime:
        """Gets the posted of this Article.


        :return: The posted of this Article.
        :rtype: datetime
        """
        return self._posted

    @posted.setter
    def posted(self, posted: datetime):
        """Sets the posted of this Article.


        :param posted: The posted of this Article.
        :type posted: datetime
        """

        self._posted = posted

    @property
    def modified(self) -> datetime:
        """Gets the modified of this Article.


        :return: The modified of this Article.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified: datetime):
        """Sets the modified of this Article.


        :param modified: The modified of this Article.
        :type modified: datetime
        """

        self._modified = modified

    @property
    def published(self) -> datetime:
        """Gets the published of this Article.


        :return: The published of this Article.
        :rtype: datetime
        """
        return self._published

    @published.setter
    def published(self, published: datetime):
        """Sets the published of this Article.


        :param published: The published of this Article.
        :type published: datetime
        """

        self._published = published

    @property
    def tags(self) -> List[str]:
        """Gets the tags of this Article.


        :return: The tags of this Article.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags: List[str]):
        """Sets the tags of this Article.


        :param tags: The tags of this Article.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def alias(self) -> str:
        """Gets the alias of this Article.


        :return: The alias of this Article.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias: str):
        """Sets the alias of this Article.


        :param alias: The alias of this Article.
        :type alias: str
        """

        self._alias = alias