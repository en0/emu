from emu.param_acsr.param_accessor import ParamAccessor


class AxAccessor(ParamAccessor):
    def read(self) -> int:
        if self._desc.by_ref:
            return self._ram.get(self._core.ax)
        else:
            return self._core.ax

    def write(self, val: int):
        if  self._desc.by_ref:
            self._ram.set(self._core.ax, val)
        else:
            self._core.ax = val
