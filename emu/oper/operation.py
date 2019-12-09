from abc import ABC, abstractmethod
from emu.contract import IExecutionUnit


class Operation(ABC):
    @abstractmethod
    def execute(self, eu: IExecutionUnit, *args) -> bool:
        raise NotImplementedError()
