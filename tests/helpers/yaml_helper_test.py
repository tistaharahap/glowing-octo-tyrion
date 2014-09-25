from tests.base_test import BaseTest
from app.helpers import read_yaml
from nose.tools import raises, ok_, eq_
from app.errors import ConfigNotFoundError


class YamlHelperTest(BaseTest):

    def test_read_yaml(self):
        path = 'app/config/config.yml'
        config = read_yaml(path)

        ok_(isinstance(config, dict),
            msg='Returned object must be an instance of dict')
        ok_(len(config.keys()) > 0,
            msg='Returned object must not be empty')

    @raises(ConfigNotFoundError)
    def test_read_yaml_imaginary_file_should_raises_error(self):
        path = '/a/b/s/c.yml'
        config = read_yaml(path)
