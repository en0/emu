from typing import List

from emu.contract import IRam


class Ram(IRam):
    def __init__(self, size: int):
        self._data = [0] * size

    def get(self, offset) -> int:
        ## TODO: Deal with memory reference error
        return self._data[offset]

    def set(self, offset: int, value: int):
        ## TODO: Deal with memory reference error
        self._data[offset] = value

