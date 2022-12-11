from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    items: list
    operation: Callable[[int], int]
    test: int
    true: int
    false: int
    worry: int = 0
    inspection_count: int = 0
