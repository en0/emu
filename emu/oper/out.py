from emu.oper.operation import Operation
from emu.contract import IExecutionUnit


class OutOp(Operation):
    @property
    def suffixes(self) -> int:
        return 0b11

    @property
    def code(self) -> int:
        return 0b00000100

    def execute(self, eu: IExecutionUnit, *args) -> bool:
        value, port = args
        eu.write_port(port, value)
        return True
