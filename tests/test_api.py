"""Token Service: test blueprint."""

import json
import unittest

from tokensrv.service import ADMIN_ROLE, ADMIN_TOKEN, ADMIN_USERNAME,\
    USER_ROLE, USER_TOKEN, USER_USERNAME
from tokensrv.command_handlers import create_app


API_ROOT = '/api/v1'


class TestApiMock(unittest.TestCase):
    """Test cases to check the API mock."""

    def test_status(self):
        """Test liveness probe."""
        with create_app().test_client() as client:
            response = client.get(f'{API_ROOT}/alive')
            self.assertEqual(response.status_code, 204)

    def test_token_admin(self):
        """Test get admin token."""
        with create_app().test_client() as client:
            response = client.get(f'{API_ROOT}/token/{ADMIN_TOKEN}')
            self.assertEqual(response.status_code, 200)
            response_data = json.loads(response.data)
            self.assertIn('username', response_data)
            self.assertEqual(response_data['username'], ADMIN_USERNAME)
            self.assertIn('roles', response_data)
            self.assertEqual([ADMIN_ROLE, USER_ROLE], response_data['roles'])

    def test_token_user(self):
        """Test get user token."""
        with create_app().test_client() as client:
            response = client.get(f'{API_ROOT}/token/{USER_TOKEN}')
            self.assertEqual(response.status_code, 200)
            response_data = json.loads(response.data)
            self.assertIn('username', response_data)
            self.assertEqual(response_data['username'], USER_USERNAME)
            self.assertIn('roles', response_data)
            self.assertEqual([USER_ROLE], response_data['roles'])

    def test_wrong_token(self):
        """Test get wrong token."""
        with create_app().test_client() as client:
            response = client.get(f'{API_ROOT}/token/wrong_token')
            self.assertEqual(response.status_code, 404)
