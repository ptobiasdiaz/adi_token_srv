'''
    Token Service: blue print of the API
'''
import json

from tokensrv.service import TokenNotFound
from flask import Blueprint, current_app, Response

ApiMock = Blueprint('token_service', __name__)
API_ROOT = '/api/v1'


@ApiMock.route(f'{API_ROOT}/alive', methods=('GET',))
def live_probe() -> Response:
    '''Use to make probes'''
    return Response('', status=204)

@ApiMock.route(f'{API_ROOT}/token/<token>', methods=('GET',))
def get_token_info(token: str) -> Response:
    '''Get token info'''
    try:
        owner = current_app.config['service'].token_owner(token)
        roles = current_app.config['service'].token_roles(token)
    except TokenNotFound:
        return Response('Token not found', status=404)
    return Response(json.dumps({
        'username': owner,
        'roles': roles
    }), status=200)
