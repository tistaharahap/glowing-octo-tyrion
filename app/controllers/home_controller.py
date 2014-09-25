from flask.views import MethodView
from flask import render_template, current_app
from app.helpers import compile_assets
from app.services import BankService
from app.libraries import KlikBCA


class HomeController(MethodView):

    def __init__(self):
        compile_assets(app=current_app,
                       controller_name='home')

    def get(self):
        bank_service = BankService(bank_lib=KlikBCA())

        first_of_month = bank_service.mutation_since_first_of_month()

        return render_template('home.html',
                               saldo=first_of_month.get('saldo'),
                               transactions=first_of_month.get('transaction'))
