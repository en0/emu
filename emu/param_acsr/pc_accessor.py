from emu.param_acsr.param_accessor import ParamAccessor


class PcAccessor(ParamAccessor):
    def read(self) -> int:
        if self._desc.by_ref:
            return self._ram.get(self._core.pc)
        else:
            return self._core.pc

    def write(self, val: int):
        if  self._desc.by_ref:
            self._ram.set(self._core.pc, val)
        else:
            self._core.pc = val
