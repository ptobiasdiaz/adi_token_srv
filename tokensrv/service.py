'''
    Token Service: service (mock)
'''

from typing import List


ADMIN_TOKEN = 'token_for_admin'
ADMIN_USERNAME = 'administrator'
ADMIN_ROLE = 'admin'
USER_TOKEN = 'token_for_user'
USER_USERNAME = 'user'
USER_ROLE = 'user'


class TokenNotFound(Exception):
    '''Raised if given token does not exists'''
    def __init__(self, token: str) -> None:
        self._tk_ = token

    def __str__(self) -> str:
        return f'Invalid token: {self._tk_}'


class ServiceMock:
    '''Mock implementation of the service'''
    def token_owner(self, token: str) -> str:
        '''Get the owner of a given token'''
        if token == ADMIN_TOKEN:
            return ADMIN_USERNAME
        if token == USER_TOKEN:
            return USER_USERNAME
        raise TokenNotFound(token)

    def token_roles(self, token: str) -> List[str]:
        '''Get the list of roles of a given token'''
        if token == ADMIN_TOKEN:
            return [ADMIN_ROLE, USER_ROLE]
        if token == USER_TOKEN:
            return [USER_ROLE]
        raise TokenNotFound(token)
