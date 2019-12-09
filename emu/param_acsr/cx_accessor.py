from emu.param_acsr.param_accessor import ParamAccessor


class CxAccessor(ParamAccessor):
    def read(self) -> int:
        if self._desc.by_ref:
            return self._ram.get(self._core.cx)
        else:
            return self._core.cx

    def write(self, val: int):
        if  self._desc.by_ref:
            self._ram.set(self._core.cx, val)
        else:
            self._core.cx = val
