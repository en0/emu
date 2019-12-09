from emu.param_acsr.param_accessor import ParamAccessor


class BxAccessor(ParamAccessor):
    def read(self) -> int:
        if self._desc.by_ref:
            return self._ram.get(self._core.bx)
        else:
            return self._core.bx

    def write(self, val: int):
        if  self._desc.by_ref:
            self._ram.set(self._core.bx, val)
        else:
            self._core.bx = val
