from emu.oper.operation import Operation
from emu.contract import IExecutionUnit
from emu.const import FLG_CORE_HLT


class HltOp(Operation):
    def execute(self, eu: IExecutionUnit, *args) -> bool:
        eu.set_flag(FLG_CORE_HLT)
        return False

