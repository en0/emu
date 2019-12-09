from abc import ABC, abstractmethod

from emu.core import Core
from emu.param_desc import ParamDescriptor
from emu.contract import IRam, IRom


class ParamAccessor(ABC):
    _desc: ParamDescriptor
    _core: Core
    _rom: IRom
    _ram: IRam

    def __init__(self, core: Core, rom: IRom, ram: IRam):
        self._core = core
        self._rom = rom
        self._ram = ram
        self._desc = None

    def __repr__(self):
        return self._desc.__repr__() + ":" + self.__class__.__name__

    def set_desc(self, desc: ParamDescriptor):
        self._desc = desc

    @property
    def offset(self) -> int:
        return self._desc.offset

    @abstractmethod
    def read(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def write(self, val: int):
        raise NotImplementedError()

