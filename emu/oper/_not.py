from emu.oper.operation import Operation
from emu.contract import IExecutionUnit


class NotOp(Operation):
    def execute(self, eu: IExecutionUnit, *args) -> bool:
        a, _ = args
        eu.store(~a)
        return True
