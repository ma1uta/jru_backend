# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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
from backend.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_articles(self):
        """Test case for get_articles

        get articles
        """
        response = self.client.open(
            '/api/v2/json/articles',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_domains(self):
        """Test case for get_domains

        get domains
        """
        response = self.client.open(
            '/api/v2/json/domains',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_logout(self):
        """Test case for get_logout

        logout
        """
        response = self.client.open(
            '/api/v2/json/logout',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_roster(self):
        """Test case for get_roster

        get the roster
        """
        response = self.client.open(
            '/api/v2/json/roster',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_settings(self):
        """Test case for get_settings

        get MAM settings
        """
        response = self.client.open(
            '/api/v2/json/mam/settings',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vcard(self):
        """Test case for get_vcard

        get user vcard
        """
        response = self.client.open(
            '/api/v2/json/vcard',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_feedback(self):
        """Test case for post_feedback

        sent a feedback
        """
        body = Feedback()
        response = self.client.open(
            '/api/v2/json/feedback',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_login(self):
        """Test case for post_login

        login
        """
        body = Auth()
        response = self.client.open(
            '/api/v2/json/auth',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_messages(self):
        """Test case for post_messages

        get mam messages
        """
        body = MAMMessageRequest()
        response = self.client.open(
            '/api/v2/json/mam/messages',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_register(self):
        """Test case for post_register

        register
        """
        body = Register()
        response = self.client.open(
            '/api/v2/json/register',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_reset(self):
        """Test case for post_reset

        reset password
        """
        body = Register()
        response = self.client.open(
            '/api/v2/json/reset',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_setemail(self):
        """Test case for post_setemail

        set an email
        """
        body = Register()
        response = self.client.open(
            '/api/v2/json/setemail',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_settings(self):
        """Test case for post_settings

        set MAM settings
        """
        body = MAMSettings()
        response = self.client.open(
            '/api/v2/json/mam/settings',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
