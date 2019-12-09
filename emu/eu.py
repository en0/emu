from emu.util import itob, check_flag, mask_off
from emu.core import Core
from emu.param_desc import ParamDescriptor
from emu.param_acsr import AccessorCatalog, ParamAccessor
import emu.const as const
from emu.oper import OperationCatalog, Operation
from emu.contract import IExecutionUnit, IBus, IRom, IRam


class ExecutionUnit(IExecutionUnit):

    def __init__(self, core: Core, rom: IRom, ram: IRam, bus: IBus, accessor_catalog: AccessorCatalog, operation_catalog: OperationCatalog):
        self._core = core
        self._rom = rom
        self._ram = ram
        self._bus = bus
        self._accessors = accessor_catalog
        self._operations = operation_catalog

        self._instruction: int = 0
        self._code: int = 0
        self._src: ParamAccessor = None
        self._dst: ParamAccessor = None
        self._operation: Operation = None

    def __repr__(self):
        return f"<ExecutionUnit OpCode={self._code}>"

    def dumps(self):
        op = "unknown" if self._operation is None else self._operation.__class__.__name__
        return "\n".join([
            "ExecutionUnit Dump ------------",
            f" MNE: {itob(self._instruction)} [{op}] ",
            f" SRC: {str(self._src)}",
            f" DST: {str(self._dst)}",
        ])

    def dump_core(self):
        print(self._core.dumps(),"\n")
        print(self.dumps())

    def load(self):
        self._instruction = self._rom.get(self._core.pc)
        self._code = mask_off(const.MSK_OPCODE, self._instruction)
        src_desc = ParamDescriptor(mask_off(0xF000, self._instruction) >> 12)
        dst_desc = ParamDescriptor(mask_off(0x0F00, self._instruction) >> 8)
        dst_desc.offset += src_desc.offset
        self._src = self._accessors.get(src_desc)
        self._dst = self._accessors.get(dst_desc)
        self._operation = self._operations.get(self._code)

    def execute(self):
        if self._execute():
            self._increment_pc()

    def _execute(self) -> bool:
        if self._conditions_met():
            args = [self._src.read(), self._dst.read()]
            return self._operation.execute(self, *args)
        else:
            return True

    def _increment_pc(self):
        self._core.pc += max(self._src.offset, self._dst.offset) + 1

    def _conditions_met(self) -> bool:
        if mask_off(const.MSK_CONDITIONS_ENABLED, self._instruction) == 0:
            # No conditions required
            return True

        # Some condition required

        if check_flag(const.FLG_CONDITIONS_EQ_ENABLED, self._instruction):
            # Equality is allowed to satisify condition
            test_value = mask_off(const.MSK_CONDITIONS_EQ_VALUE, self._instruction) > 0
            actual_value = mask_off(const.FLG_CORE_EQ, self._core.flg) > 0
            if test_value == actual_value:
                return True

        if not check_flag(const.FLG_CONDITIONS_LG_ENABLED, self._instruction):
            # LT/GT doesn't qualify, so no conditions met.
            return False

        # LT or GT is allowed to satisify condition

        if (mask_off(const.MSK_CONDITIONS_LG_VALUE, self._instruction) > 0):
            # GT Condition is allowed to satisify condition
            if self.get_flag(const.FLG_CORE_GT):
                return True
        else:
            # LT Condition is allowed to satisify condition
            if self.get_flag(const.FLG_CORE_LT):
                return True

    def store(self, val: int):
        self._dst.write(val)

    def write_port(self, port: int, value: int):
        self._bus.write(port, value)

    def has_input(self, port: int) -> bool:
        return self._bus.peek(port) is not None

    def read_port(self, port: int) -> int:
        return self._bus.read(port) or 0

    def set_flag(self, flag: int):
        self._core.flg |= flag

    def clear_flag(self, flag: int):
        self._core.flg &= ~flag

    def get_flag(self, flag: int) -> bool:
        return check_flag(flag, self._core.flg)


if __name__ == "__main__":
    from emu.bus import Bus
    from emu.rom import Rom
    from emu.ram import Ram
    core = Core()

    #
    # 0  xor ax, ax  0000 0000 0000 1111,
    # 1  in 0, bx    0111 0001 0000 0001, 0x00,
    # 3  add bx, ax  0001 0000 0000 1000,
    # 4  cmp 10, ax  0111 0000 0000 0010, 0x0A
    # 6  jle $hlt    0111 0110 1110 0011, 0x0A,
    # 8  jmp 3       0111 0110 0000 0011, 0x03,
    # a  out ax, 0   0000 0111 0000 0100, 0x00,
    # c  hlt         0000 0000 0000 0110,
    #


    prog = [
        0b0000000000001111,
        0b0111000100000101, 0x00,
        0b0001000000001000,
        0b0111000000000010, 0x0A,
        0b0111011011100011, 0x0A,
        0b0111011000000011, 0x03,
        0b0000011100000100, 0x00,
        0b0000000000000110,
    ]

    rom = Rom(prog)
    ram = Ram(10)
    bus = Bus()
    af = AccessorCatalog(core, rom, ram)
    of = OperationCatalog()

    eu = ExecutionUnit(core, rom, ram, bus, af, of)

    bus.write(0, 1)

    while (core.flg & 1) == 0:
        eu.load()
        #eu.dump_core()
        #print("#######################################################")
        #input("...")
        eu.execute()

    eu.dump_core()
    print("Result:", bus.read(0))
