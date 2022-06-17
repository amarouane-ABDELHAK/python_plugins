import json
from dataclasses import dataclass
import game.factory as fact
from game.charachter import GaneCharachter
from game.loader import load_plogins

@dataclass
class Sorcerer:
    name: str
    def make_noise(self) -> None:
        print("Abbra Kadabraa")


@dataclass
class Wizard:
    name: str
    def make_noise(self) -> None:
        print("Run you fouls")

@dataclass
class Witcher:
    name: str
    def make_noise(self) -> None:
        print("Is there a job for a witcher?")


def main() -> None:
    fact.register('wizard', Wizard)
    fact.register('sorcerer', Sorcerer)
    fact.register('witcher', Witcher)
    with open("./level.json", "r") as _file:
        data = json.load(_file)
    load_plogins(data['plugins'])
    charachters: list[GaneCharachter] = [fact.create(item) for item in data['charachters']]
    for charachter in charachters:
        print(charachter, end="\t")
        charachter.make_noise()
if __name__ == "__main__":
    main()