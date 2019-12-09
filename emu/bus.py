from typing import Union

from emu.contract import IBus


class QueuedBus(IBus):
    def __init__(self):
        self._ports = dict()

    def read(self, port: int) -> Union[int, None]:
        self._ports.setdefault(port, [])
        try:
            return self._ports[port].pop(0)
        except IndexError:
            return None

    def peek(self, port: int) -> Union[int, None]:
        self._ports.setdefault(port, [])
        try:
            return self._ports[port][0]
        except IndexError:
            return None

    def write(self, port: int, value: int):
        self._ports.setdefault(port, [])
        self._ports[port].append(value)

    def dumps(self):
        return "\n".join([
            f"{str(p)}: [{', '.join([str(_) for _ in v])}]"
            for p, v in self._ports.items()
        ])


class Bus(IBus):
    def __init__(self):
        self._ports = dict()

    def read(self, port: int) -> Union[int, None]:
        value = self._ports.get(port)
        self._ports[port] = None
        return value

    def peek(self, port: int) -> Union[int, None]:
        return self._ports.get(port)

    def write(self, port: int, value: int):
        self._ports[port] = value

    def dumps(self):
        return "\n".join([
            f"{str(p)}: {v}]"
            for p, v in self._ports.items()
        ])

