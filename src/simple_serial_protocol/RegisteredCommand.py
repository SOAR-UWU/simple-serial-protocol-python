from __future__ import annotations
from typing import Final

from simple_serial_protocol.ParamsParser import ParamsParser
from simple_serial_protocol.common import Byte, CommandCallback


class RegisteredCommand:
    def __init__(self, command_id: str, callback: CommandCallback, param_types: list[str] = None):
        self._command_id: Final[str] = command_id
        self._callback: CommandCallback = callback
        self._params_parser: ParamsParser | None = None
        if param_types is not None and len(param_types) > 0:
            self._params_parser = ParamsParser(param_types)

    def dispose(self) -> None:
        self._callback = None
        if self._params_parser:
            self._params_parser.dispose()

    def params_read(self) -> bool:
        return self._params_parser.is_full() if self._params_parser is not None else True

    def add_byte(self, byte: Byte) -> None:
        if self._params_parser:
            self._params_parser.add_byte(byte)

    def reset_param_parser(self) -> None:
        if self._params_parser:
            self._params_parser.reset()

    def call_callback(self) -> None:
        if self._params_parser:
            self._callback(*self._params_parser.get_data())
        else:
            self._callback()
