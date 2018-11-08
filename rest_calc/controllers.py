import datetime
from time import sleep

import calc

__all__ = ["CalcResource"]


operands = {
    'add': calc.add,
    'subtract': calc.subtract,
    'multiply': calc.multiply,
    'divide': calc.divide
}


class CalcResource:
    def on_get(self, req, res):
        sleep(1)
        op = req.get_param('op')
        a = int(req.get_param('a'))
        b = int(req.get_param('b'))
        res.media = {
            'operand': op,
            'a': a,
            'b': b,
            'result': operands[op](a, b),
            'ts': int(datetime.datetime.utcnow().timestamp())
        }
