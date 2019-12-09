from math import floor
from emu.oper.operation import Operation
from emu.contract import IExecutionUnit


class DivOp(Operation):
    def execute(self, eu: IExecutionUnit, *args) -> bool:
        a, b = args
        eu.store(floor(a / b))
        return True
