from dataclasses import dataclass

from typing import Protocol

@dataclass
class GaneCharachter(Protocol):
    """
    Basic not extra
    """
    def make_noise(self) -> None:
        pass