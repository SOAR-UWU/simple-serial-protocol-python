from typing import Callable

try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias

Byte: TypeAlias = int
CommandCallback: TypeAlias = Callable[..., None]
ErrorCallback: TypeAlias = Callable[[Exception], None]
