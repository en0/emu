from emu.oper.operation import Operation
from emu.contract import IExecutionUnit
from emu.const import FLG_CORE_HLT


class BrkOp(Operation):
    def execute(self, eu: IExecutionUnit, *args) -> bool:
        eu.dump_core()
        input("...")
        return True
