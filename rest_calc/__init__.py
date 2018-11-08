import falcon
from rest_calc.controllers import *

api = falcon.API()
api.add_route('/calc', CalcResource())
