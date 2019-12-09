import emu.const as const
from emu.oper.operation import Operation
from emu.oper.nop import NoOp
from emu.oper.mov import MovOp
from emu.oper.cmp import CmpOp
from emu.oper.jmp import JmpOp
from emu.oper.out import OutOp
from emu.oper._in import InOp
from emu.oper.hlt import HltOp
from emu.oper.brk import BrkOp
from emu.oper.add import AddOp
from emu.oper.sub import SubOp
from emu.oper.mul import MulOp
from emu.oper.div import DivOp
from emu.oper._not import NotOp
from emu.oper._and import AndOp
from emu.oper._or import OrOp
from emu.oper._xor import XorOp


__operations__ = {
        const.OPCODE_NOP: NoOp,
        const.OPCODE_MOV: MovOp,
        const.OPCODE_CMP: CmpOp,
        const.OPCODE_JMP: JmpOp,
        const.OPCODE_OUT: OutOp,
        const.OPCODE_IN:  InOp,
        const.OPCODE_HLT: HltOp,
        const.OPCODE_BRK: BrkOp,
        const.OPCODE_ADD: AddOp,
        const.OPCODE_SUB: SubOp,
        const.OPCODE_MUL: MulOp,
        const.OPCODE_DIV: DivOp,
        const.OPCODE_NOT: NotOp,
        const.OPCODE_AND: AndOp,
        const.OPCODE_OR:  OrOp,
        const.OPCODE_XOR: XorOp,
}


class OperationCatalog:
    def __init__(self):
        self._opers = {k: v() for k, v in __operations__.items()}

    def get(self, opcode: int) -> Operation:
        oper = self._opers.get(opcode)
        if oper is None:
            # TODO: This should be a unknown opcode excetpion
            raise RuntimeError(f"Unknown opcode {opcode}")
        return oper

__all__ = [ "OperationCatalog", "Operation" ]


