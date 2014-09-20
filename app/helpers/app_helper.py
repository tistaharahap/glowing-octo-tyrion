from flask import Flask
from app.helpers import read_yaml, read_env
from app.errors import HTTPMethodNotImplementedError, ControllerNotFoundError, ConfigNotFoundError
import importlib


#if __name__ != '__main__':
config = read_yaml('app/config/config.yml')
routes = read_yaml('app/config/routes.yml')

env = config.get(read_env())
flask_config = env.get('flask') if env else None

def create_app(config=config, env=env):
    if not config:
        raise ConfigNotFoundError('Config is not available')
    if not env:
        raise ConfigNotFoundError('Environment is not set')

    app = Flask(__name__)
    app.config['DEBUG'] = env['flask']['debug']
    app.config['SECRET_KEY'] = env['flask']['secret_key']

    create_routes(app)

    return app

def create_routes(app, app_routes=routes):
    if not app_routes:
        raise ConfigNotFoundError('Routes are empty')

    for (k, v) in app_routes.iteritems():
        route = app_routes[k]

        try:
            loaded_mod = load_class('app.controllers.%sController' % route['controller'].title())
        except AttributeError:
            raise ControllerNotFoundError('Class %sController is not found' % route['controller'].title())

        clsmethods = dir(loaded_mod)
        for method in route['methods']:
            method = method.lower()
            if method not in clsmethods:
                raise HTTPMethodNotImplementedError('Class %sController is not implementing method %s' % (route['controller'].title(), method.upper()))

        app.add_url_rule(route['uri'],
                         view_func=loaded_mod.as_view('%s_controller' % route['controller']),
                         methods=route['methods'])

def load_class(full_class_string):
    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]

    module = importlib.import_module(module_path)
    return getattr(module, class_str)
