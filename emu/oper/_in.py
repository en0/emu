from emu.oper.operation import Operation
from emu.contract import IExecutionUnit


class InOp(Operation):
    def execute(self, eu: IExecutionUnit, *args) -> bool:
        port, dest = args
        if eu.has_input(port):
            value = eu.read_port(port)
            eu.store(value)
            return True
        return False
