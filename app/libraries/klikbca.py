from online_banking_abstracts import OnlineBankingAbstracts
from datetime import date
from flask import current_app
from app.errors import ConfigNotFoundError
import requests


class KlikBCA(OnlineBankingAbstracts):

    url = None

    username = None
    password = None

    def __init__(self, testing_app=None):
        app = testing_app
        if not app:
            raise ValueError('If you set testing_app parameter, please make sure it\'s not None')
        if not app.config.get('TESTING'):
            app = current_app._get_current_object()


        try:
            klikbca_config = app.config.get('ENV').get('klikbca')
        except AttributeError:
            raise AttributeError('The parameter testing_app is an improper app object')
        if not klikbca_config:
            raise ConfigNotFoundError('KlikBCA config is not valid')

        self.username = klikbca_config.get('username')
        self.password = klikbca_config.get('password')
        self.url = klikbca_config.get('url')

    def mutation_history(self, start_date, end_date):
        if not isinstance(start_date, date):
            raise TypeError('The parameter start_date must be an instance of date')
        if not isinstance(end_date, date):
            raise TypeError('The parameter end_date must be an instance of date')

        endpoint = "%sranged/%s-%s-%s/%s-%s-%s" % (self.url, start_date.year, start_date.month,
                                                   start_date.day, end_date.year, end_date.month,
                                                   end_date.day)

        r = requests.get(endpoint)
        if not (r.status_code >= 200 and r.status_code < 300):
            raise EnvironmentError('The KlikBCA service is not responding')

        return r.json()
