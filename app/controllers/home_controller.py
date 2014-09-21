from flask.views import MethodView
from flask import render_template, current_app
from app.helpers import compile_assets


class HomeController(MethodView):

    def __init__(self):
        compile_assets(app=current_app,
                       controller_name='home')

    def get(self):
        return render_template('index.html')
