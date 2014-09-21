from flask import Flask
from flask.ext.assets import Environment, Bundle
from app.helpers import read_yaml, read_env
from app.errors import HTTPMethodNotImplementedError, ControllerNotFoundError, ConfigNotFoundError
import importlib
import os.path


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

    tpl_folder = os.path.abspath('templates')
    static_folder = os.path.abspath('static')

    app = Flask(__name__,
                template_folder=tpl_folder,
                static_folder=static_folder,
                static_url_path='/s')
    app.config['DEBUG'] = env['flask']['debug']
    if app.config['DEBUG'] is True:
        app.config['ASSETS_DEBUG'] = True

    app.config['SECRET_KEY'] = env['flask']['secret_key']

    create_routes(app)

    return app

def compile_assets(app, controller_name):
    if not isinstance(app, Flask):
        raise TypeError('The parameter app must be an instance of Flask')
    if not isinstance(controller_name, str):
        raise TypeError('The parameter controller_name must be an instance of String')
    if len(controller_name) == 0:
        raise ValueError('The parameter controller_name must have a length of more than 0')

    assets = Environment(app)

    js = compile_js(controller_name)

    assets.register('js_all', js)

def compile_js(controller_name):
    if not isinstance(controller_name, str):
        raise TypeError('The parameter controller_name must be an instance of String')
    if len(controller_name) == 0:
        raise ValueError('The parameter controller_name must have a length of more than 0')

    coffee_path = 'coffee/'

    static_abs_path = os.path.abspath('static')
    bundle = ['%smain.coffee' % coffee_path]

    controller_coffee_path = '%s/coffee/%s.coffee' % (static_abs_path, controller_name)
    if os.path.isfile(controller_coffee_path):
        bundle.append('%s%s.coffee' % (coffee_path, controller_name))

    js = Bundle(*bundle,
                filters='coffeescript,rjsmin',
                output='out/a.js')

    return js

def compile_css(controller_name):
    pass

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

        #compile_assets(app, route['controller'])

def load_class(full_class_string):
    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]

    module = importlib.import_module(module_path)
    return getattr(module, class_str)
