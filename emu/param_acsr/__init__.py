from emu.core import Core
from emu.rom import Rom
from emu.ram import Ram
from emu.param_desc import ParamDescriptor
from emu.param_acsr.rom_accessor import RomAccessor
from emu.param_acsr.ax_accessor import AxAccessor
from emu.param_acsr.bx_accessor import BxAccessor
from emu.param_acsr.cx_accessor import CxAccessor
from emu.param_acsr.dx_accessor import DxAccessor
from emu.param_acsr.pc_accessor import PcAccessor
from emu.param_acsr.sp_accessor import SpAccessor
from emu.param_acsr.param_accessor import ParamAccessor
import emu.const as const


__accessors__ = {
    const.ROM_SEL: RomAccessor,
    const.AX_SEL:  AxAccessor,
    const.BX_SEL:  BxAccessor,
    const.CX_SEL:  CxAccessor,
    const.DX_SEL:  DxAccessor,
    const.PC_SEL:  PcAccessor,
    const.SP_SEL:  SpAccessor
}


class AccessorCatalog:
    def __init__(self, core: Core, rom: Rom, ram: Ram):
        self._accessors = {k: v(core, rom, ram) for k, v in __accessors__.items()}

    def get(self, desc: ParamDescriptor):
        accessor =  self._accessors.get(desc.sel)
        if accessor is None:
            # TODO: This should be an panic
            raise Runtime(f"Unrecognized selector: {desc.sel}")
        accessor.set_desc(desc)
        return accessor


__all__ = [ "AccessorCatalog", "ParamAccessor" ]
