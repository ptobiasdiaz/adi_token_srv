'''
    Token Service: test mock (use as example)
'''

import unittest

from tokensrv.service import ServiceMock as Service
from tokensrv.service import TokenNotFound


class TestServiceMock(unittest.TestCase):
    '''Test cases to check the mock'''

    def test_owner_of_admin_token(self):
        '''Test admin token'''
        self.assertEqual(Service().token_owner('token_for_admin'), 'administrator')

    def test_owner_of_user_token(self):
        '''Test user token'''
        self.assertEqual(Service().token_owner('token_for_user'), 'user')

    def test_wrong_token(self):
        '''Test wrong token'''
        with self.assertRaises(TokenNotFound):
            Service().token_owner('other_token')

    def test_roles_of_admin(self):
        '''Test admin roles'''
        self.assertIn('admin', Service().token_roles('token_for_admin'))
        self.assertIn('user', Service().token_roles('token_for_admin'))
        self.assertEqual(len(Service().token_roles('token_for_admin')), 2)

    def test_roles_of_user(self):
        '''Test user roles'''
        self.assertIn('user', Service().token_roles('token_for_user'))
        self.assertEqual(len(Service().token_roles('token_for_user')), 1)
