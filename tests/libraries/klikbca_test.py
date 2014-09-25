from tests.base_test import BaseTest
from app.libraries import KlikBCA
from app.errors import ConfigNotFoundError
from nose.tools import raises, ok_
import mock
import app


class App(object):
    pass


class KlikbcaTest(BaseTest):

    def test_init(self):
        app = App()
        app.config = {
            'ENV': {
                'klikbca': {
                    'username': 'testuser',
                    'password': '000000',
                    'url': 'http://localhost'
                }
            },
            'TESTING': True
        }
        kb = KlikBCA(testing_app=app)

    @raises(ConfigNotFoundError)
    def test_init_with_empty_klikbca_config_raises_error(self):
        app = App()
        app.config = {
            'ENV': {},
            'TESTING': True
        }
        kb = KlikBCA(testing_app=app)

    @raises(ValueError)
    def test_init_with_none_testing_app_raises_error(self):
        kb = KlikBCA(testing_app=None)

    @raises(AttributeError)
    def test_init_with_improper_testing_app_raises_error(self):
        kb = KlikBCA(testing_app={'a': 'b'})

    @mock.patch('app.libraries.KlikBCA')
    def test_mutation_history(self, mock_klikbca):
        obj = mock_klikbca()
        obj.mutation_history(start_date=obj.today(),
                             end_date=obj.today())

        ok_(mock_klikbca is app.libraries.KlikBCA,
            msg='The mocked object is not KlikBCA object')
