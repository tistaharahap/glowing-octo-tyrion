from tests.base_test import BaseTest
from app.helpers import create_app, create_routes, load_class
from nose.tools import raises, ok_, eq_
from flask import Flask


class AppHelperTest(BaseTest):

    app_for_test = None

    def test_load_class_success(self):
        full_str = "app.errors.KlikBCAError"

        klazz = load_class(full_str)

        eq_(klazz.__name__, 'KlikBCAError',
            msg='Different class name than what\'s being intended to load')

    @raises(AttributeError)
    def test_load_class_raises_attribute_error(self):
        full_str = "app.errors.SomeClass"
        klazz = load_class(full_str)

    def test_create_app(self):
        app = create_app()
        ok_(isinstance(app, Flask),
            msg='The app must be a Flask instance')

    def test_create_routes(self):
        app = Flask(__name__)
        create_routes(app)

        count = 0
        for rule in app.url_map.iter_rules():
            count += 1

        ok_(count > 1,
            msg='Routes are not implemented')
