from abc import ABC, abstractmethod
from typing import Union, List


class IExecutionUnit(ABC):
    @abstractmethod
    def store(self, val: int):
        raise NotImplementedError()

    @abstractmethod
    def write_port(port: int, value: int):
        raise NotImplementedError()

    @abstractmethod
    def has_input(port: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def read_port(port: int) -> int:
        raise NotImplementedError()

    @abstractmethod
    def set_flag(flag: int):
        raise NotImplementedError()

    @abstractmethod
    def clear_flag(flag: int):
        raise NotImplementedError()

    @abstractmethod
    def get_flag(flag: int) -> bool:
        raise NotImplementedError()


class IBus(ABC):
    @abstractmethod
    def read(self, port: int) -> Union[int, None]:
        raise NotImplementedError()

    @abstractmethod
    def peek(self, port: int) -> Union[int, None]:
        raise NotImplementedError()

    @abstractmethod
    def write(self, port: int, value: int):
        raise NotImplementedError()

    @abstractmethod
    def dumps(self):
        raise NotImplementedError()


class IRam(ABC):
    @abstractmethod
    def get(self, offset) -> int:
        raise NotImplementedError()

    @abstractmethod
    def set(self, offset: int, value: int):
        raise NotImplementedError()


class IRom(ABC):
    @abstractmethod
    def get(self, offset) -> int:
        raise NotImplementedError()
