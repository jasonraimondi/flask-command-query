import importlib
import inspect

from infrastructure.lib.command_interface import CommandInterface
from infrastructure.lib.command_handler_interface import CommandHandlerInterface
from infrastructure.repository.repository_factory import RepositoryFactory


class Mapper(object):
    def __init__(self, repository_factory: RepositoryFactory):
        self.repository_factory = repository_factory

    def handler_for(self, command: CommandInterface) -> CommandHandlerInterface:
        command_handler_name = command.__class__.__name__ + 'Handler'
        handler_class = getattr(self._get_handler_module(command), command_handler_name)

        constructor_params_list = self._get_constructor_parameter_list(command, handler_class)

        return handler_class(*constructor_params_list)

    def _get_constructor_parameter_list(self, command, handler_class):
        constructor_params_array = []

        for param in list(inspect.signature(handler_class.__init__).parameters.keys()):
            if param == 'self':
                continue

            if param == 'command':
                constructor_params_array.append(command)
            elif param == 'tweet_repository':
                constructor_params_array.append(self.repository_factory.tweet_repository())

        return constructor_params_array

    def _get_handler_module(self, command):
        command_module_name = inspect.getmodule(command).__name__
        handler_module_name = command_module_name.replace('action', 'action_handler') + '_handler'
        return importlib.import_module(handler_module_name)
