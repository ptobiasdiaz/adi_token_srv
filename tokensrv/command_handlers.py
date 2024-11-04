"""Token Service: entry points."""

from tokensrv.service import ServiceMock as Service
from tokensrv.blueprint import ApiMock as Api

from flask import Flask


def create_app():
    """Instance flask app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config['service'] = Service()
    app.register_blueprint(Api)
    return app

def run_server():
    """Instance flask app and run it."""
    return create_app().run(host='0.0.0.0', port=3002, debug=True)
