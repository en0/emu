from emu.util import check_flag, mask_off, itob
from emu.const import (
    FLG_BYREF,
    MSK_PARAM,
    ROM_SEL)


class ParamDescriptor:
    def __init__(self, param_desc: int):
        self.by_ref = check_flag(FLG_BYREF, param_desc)
        self.sel = mask_off(MSK_PARAM, param_desc)
        self.in_rom = self.sel == ROM_SEL
        self._offset = 1 if self.in_rom else 0

    @property
    def offset(self) -> int:
        return self._offset if self.in_rom else 0

    @offset.setter
    def offset(self, value: int):
        self._offset = value

    def __repr__(self):
        return "".join([
            "[",
            "R" if self.by_ref else "-",
            "I" if self.in_rom else "-",
            "]",
            f" {itob(self.sel, 4)}:{self.offset}",
        ])
