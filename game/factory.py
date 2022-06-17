from typing import Callable, Any
from game.charachter import GaneCharachter

character_creation_functs: dict[str, Callable[..., GaneCharachter]] = {}

def register(charachter_type:str, creation_func:  Callable[..., GaneCharachter]):
    """Register a new charachter type"""
    character_creation_functs[charachter_type] = creation_func

def unregister(charachter_type:str):
    """Register a new charachter type"""
    character_creation_functs.pop(charachter_type, False)

def create(arguments: dict[str, Any]) -> GaneCharachter:

    arguments_copy = arguments.copy()
    charachter_type = arguments_copy.pop('type')
    try:
        creation_funct = character_creation_functs[charachter_type]
        return creation_funct(**arguments_copy)
    except KeyError:
        raise ValueError(f"Unkown Charachter type {charachter_type}")
