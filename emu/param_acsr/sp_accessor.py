from emu.param_acsr.param_accessor import ParamAccessor


class SpAccessor(ParamAccessor):
    def read(self) -> int:
        if self._desc.by_ref:
            return self._ram.get(self._core.sp)
        else:
            return self._core.sp

    def write(self, val: int):
        if  self._desc.by_ref:
            self._ram.set(self._core.sp, val)
        else:
            self._core.sp = val
