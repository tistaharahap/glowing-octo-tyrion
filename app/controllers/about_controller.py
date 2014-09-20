from flask.views import MethodView


class AboutController(MethodView):

    def get(self):
        return 'ok'
