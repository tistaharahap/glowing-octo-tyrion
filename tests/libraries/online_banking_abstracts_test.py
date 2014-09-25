from tests.base_test import BaseTest
from app.libraries import OnlineBankingAbstracts
from nose.tools import raises, ok_


class OnlineBankingAbstractsTest(BaseTest):

    def test_has_abstract_method_mutation_history(self):
        ok_(hasattr(OnlineBankingAbstracts, 'mutation_history'),
            msg='Must have mutation_history abstract method')

        ok_(OnlineBankingAbstracts.mutation_history.__isabstractmethod__ == True,
            msg='The method mutation_history must be an abstract method')
