import importlib
import  game.factory 
class PluginInterface:
    @staticmethod
    def initilize( game_factory: game.factory) -> None:
        """Init the plugin"""

def import_module(name:str) ->  PluginInterface:
    return importlib.import_module(name)


def load_plogins(plugins:list[str]) -> None:
    """Load plugins"""
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initilize(game.factory)

