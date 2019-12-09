from emu.param_acsr.param_accessor import ParamAccessor


class RomAccessor(ParamAccessor):
    def read(self) -> int:
        if self._desc.by_ref:
            offset = self._rom.get(self._desc.offset + self._core.pc)
            return self._ram.get(offset)
        else:
            return self._rom.get(self._desc.offset + self._core.pc)

    def write(self, val: int):
        if not self._desc.by_ref:
            raise RuntimeError("Cannot write to read only memory")
        offset = self._rom.get(self._desc.offset + self._core.pc)
        self._ram.set(offset, val)
