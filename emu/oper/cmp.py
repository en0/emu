from emu.oper.operation import Operation
from emu.contract import IExecutionUnit
from emu.const import FLG_CORE_EQ, FLG_CORE_LT, FLG_CORE_GT


class CmpOp(Operation):
    def execute(self, eu: IExecutionUnit, *args) -> bool:
        a, b = args
        eu.clear_flag(FLG_CORE_EQ | FLG_CORE_LT | FLG_CORE_GT)
        if a < b:
            eu.set_flag(FLG_CORE_LT)
        if a > b:
            eu.set_flag(FLG_CORE_GT)
        if a == b:
            eu.set_flag(FLG_CORE_EQ)
        return True
