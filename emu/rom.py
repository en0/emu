from typing import List

from emu.contract import IRom


class Rom(IRom):
    def __init__(self, data: List[int]):
        self._data = data

    def get(self, offset) -> int:
        ## TODO: Deal with memory reference error
        return self._data[offset]
