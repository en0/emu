from emu.oper.operation import Operation
from emu.contract import IExecutionUnit
from emu.const import FLG_CORE_HLT


class NoOp(Operation):
    def execute(self, eu: IExecutionUnit, *args) -> bool:
        return True
