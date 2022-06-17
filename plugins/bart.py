"""Extended charachter"""

from dataclasses import dataclass

@dataclass
class Bart:
    name: str
    age: int

    def make_noise(self) -> None:
        print(f"Here is BAAAARt ({self.age})")


def initilize(whatever_here) ->  None:
    whatever_here.register('bart', Bart)