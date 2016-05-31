import flask

from . import config
from . import extensions
from . import message
from . import user


def create_app(config_name: str = 'default') -> flask.Flask:

    app = flask.Flask(__name__)

    load_config(app, config_name)
    register_extensions(app)
    register_blueprints(app)

    return app


def load_config(app: flask.Flask, config_name: str) -> None:

    app.config.from_object('app.config.{}'.format(config.config_options[config_name]))
    app.config.from_envvar('CEC_PRODUCTION_SETTINGS')


def register_extensions(app: flask.Flask) -> None:

    extensions.db.init_app(app)


def register_blueprints(app: flask.Flask) -> None:

    app.register_blueprint(user.blueprint)
    app.register_blueprint(message.blueprint)
