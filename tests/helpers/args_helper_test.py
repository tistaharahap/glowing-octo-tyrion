from tests.base_test import BaseTest
from app.helpers import read_env
from nose.tools import ok_, eq_, raises
from app.errors import NoEnvSpecifiedError
import sys


class ArgHelperTest(BaseTest):

    def test_read_env_dev(self):
        old_argv = sys.argv
        sys.argv = ['./start', 'development']

        eq_(read_env(), 'development',
            msg='The command "start development" should return development env')

        sys.argv = ['./start', 'dev']

        eq_(read_env(), 'development',
            msg='The command "start dev" should return development env')

        sys.argv = ['./start', 'debug']

        eq_(read_env(), 'development',
            msg='The command "start debug" should return development env')

    def test_read_env_stage(self):
        old_argv = sys.argv
        sys.argv = ['./start', 'stage']

        eq_(read_env(), 'staging',
            msg='The command "start stage" should return staging env')

        sys.argv = ['./start', 'staging']

        eq_(read_env(), 'staging',
            msg='The command "start staging" should return staging env')

    def test_read_env_prod(self):
        old_argv = sys.argv
        sys.argv = ['./start', 'prod']

        eq_(read_env(), 'production',
            msg='The command "start prod" should return production env')

        sys.argv = ['./start', 'production']

        eq_(read_env(), 'production',
            msg='The command "start production" should return production env')

    def test_read_env_raises_error(self):
        old_argv = sys.argv
        sys.argv = ['./start', 'waku']

        eq_(read_env(), 'test',
            msg='If environment is missing or not set properly, test env should be returned')
