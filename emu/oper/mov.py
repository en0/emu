from emu.oper.operation import Operation
from emu.contract import IExecutionUnit


class MovOp(Operation):
    def execute(self, eu: IExecutionUnit, *args) -> bool:
        value, _ = args
        eu.store(value)
        return True
