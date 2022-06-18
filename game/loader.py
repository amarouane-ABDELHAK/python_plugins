from asyncio import protocols
import importlib
from typing import Protocol
import  game.factory 


class PluginInterface(Protocol):
    """
    Protocol for typing
    """
    @staticmethod
    def initilize( _: game.factory) -> None:
        """Init the plugin"""

def import_module(name:str) ->  PluginInterface:
    """"Load stuff"""

    return importlib.import_module(name)


def load_plogins(plugins:list[str]) -> None:
    """Load plugins"""
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initilize(game.factory)

