from tests.base_test import BaseTest
from app.helpers import create_app, create_routes, load_class, compile_assets, compile_asset, ASSET_TYPE_COFFEE, ASSET_TYPE_CSS
from nose.tools import raises, ok_, eq_
from flask import Flask
from flask.ext.assets import Environment, Bundle
from app.errors import ConfigNotFoundError, HTTPMethodNotImplementedError, ControllerNotFoundError
import copy


class AppHelperTest(BaseTest):

    def test_load_class_success(self):
        full_str = "app.errors.GlowingOctoTyrionError"

        klazz = load_class(full_str)

        eq_(klazz.__name__, 'GlowingOctoTyrionError',
            msg='Different class name than what\'s being intended to load')

    @raises(AttributeError)
    def test_load_class_raises_attribute_error(self):
        full_str = "app.errors.SomeClass"
        klazz = load_class(full_str)

    def test_create_app(self):
        app = create_app()
        ok_(isinstance(app, Flask),
            msg='The app must be a Flask instance')

    @raises(ConfigNotFoundError)
    def test_create_app_no_env_should_raises_error(self):
        create_app(env=None)

    @raises(ConfigNotFoundError)
    def test_create_app_no_config_should_raises_error(self):
        create_app(config=None)

    def test_create_routes(self):
        app = Flask(__name__)
        create_routes(app)

        count = 0
        for rule in app.url_map.iter_rules():
            count += 1

        ok_(count > 1,
            msg='Routes are not implemented')

    @raises(ConfigNotFoundError)
    def test_create_routes_empty_should_raises_error(self):
        app = Flask(__name__)
        create_routes(app, app_routes=None)

    @raises(ControllerNotFoundError)
    def test_create_routes_empty_controller_should_raises_error(self):
        app = Flask(__name__)

        from app.helpers import routes
        new_routes = copy.deepcopy(routes)
        new_routes['home']['controller'] = 'r4nd0M'

        create_routes(app, app_routes=new_routes)

    @raises(HTTPMethodNotImplementedError)
    def test_create_routes_with_unimplemented_http_method_should_raises_error(self):
        app = Flask(__name__)

        from app.helpers import routes
        old_routes = copy.deepcopy(routes)

        routes['home']['methods'].append('POST')

        create_routes(app, app_routes=routes)

    @raises(TypeError)
    def test_compile_assets_with_non_string_controller_name_should_raises_error(self):
        app = Flask(__name__)
        controller_name = {}

        assets = compile_assets(app=app,
                                controller_name=controller_name)

    @raises(ValueError)
    def test_compile_assets_with_0_length_string_should_raises_error(self):
        app = Flask(__name__)
        controller_name = ''

        assets = compile_assets(app=app,
                                controller_name=controller_name)

    def test_compile_asset_coffee(self):
        controller_name = 'home'

        coffee = compile_asset(controller_name=controller_name,
                               asset_type=ASSET_TYPE_COFFEE)

        ok_(isinstance(coffee, Bundle),
            msg='Must return an instance of Bundle')

    @raises(TypeError)
    def test_compile_asset_non_string_should_raises_error(self):
        controller_name = 3

        coffee = compile_asset(controller_name=controller_name,
                               asset_type=ASSET_TYPE_COFFEE)

    @raises(ValueError)
    def test_compile_asset_0_length_string_should_raises_error(self):
        controller_name = ''

        coffee = compile_asset(controller_name=controller_name,
                               asset_type=ASSET_TYPE_COFFEE)
