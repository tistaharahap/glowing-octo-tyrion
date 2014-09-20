from flask import Flask
from app.helpers import read_yaml, read_env
from app.errors import HTTPMethodNotImplementedError, ControllerNotFoundError
import importlib


if __name__ != '__main__':
    config = read_yaml('app/config/config.yml')
    routes = read_yaml('app/config/routes.yml')

    env = config.get(read_env())
    flask_config = env['flask']

def create_app():
    global config, env

    app = Flask(__name__)
    app.config['DEBUG'] = env['flask']['debug']
    app.config['SECRET_KEY'] = env['flask']['secret_key']

    create_routes(app)

    return app

def create_routes(app):
    global routes

    for (k, v) in routes.iteritems():
        route = routes[k]

        try:
            loaded_mod = load_class('app.controllers.%sController' % k.title())
        except AttributeError:
            raise ControllerNotFoundError('Class %sController is not found' % k.title())

        clsmethods = dir(loaded_mod)
        for method in route['methods']:
            method = method.lower()
            if method not in clsmethods:
                raise HTTPMethodNotImplementedError('Class %sController is not implementing method %s' % (k.title(), method.upper()))

        app.add_url_rule(route['uri'],
                         view_func=loaded_mod.as_view('%s_controller' % k),
                         methods=route['methods'])

def load_class(full_class_string):
    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]

    module = importlib.import_module(module_path)
    return getattr(module, class_str)
