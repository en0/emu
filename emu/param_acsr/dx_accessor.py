from emu.param_acsr.param_accessor import ParamAccessor


class DxAccessor(ParamAccessor):
    def read(self) -> int:
        if self._desc.by_ref:
            return self._ram.get(self._core.dx)
        else:
            return self._core.dx

    def write(self, val: int):
        if  self._desc.by_ref:
            self._ram.set(self._core.dx, val)
        else:
            self._core.dx = val
