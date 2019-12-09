from emu.oper.operation import Operation
from emu.contract import IExecutionUnit


class OrOp(Operation):
    def execute(self, eu: IExecutionUnit, *args) -> bool:
        a, b = args
        eu.store(a | b)
        return True
