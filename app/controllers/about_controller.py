from flask.views import MethodView


class AboutController(MethodView):

    def __init__(self):
        compile_assets(app=current_app,
                       controller_name='home')

    def get(self):
        return 'ok'
