from infrastructure.lib.command_interface import CommandInterface
from infrastructure.lib.mapper import Mapper


class Bus(object):
    def __init__(self, mapper: Mapper):
        self.mapper = mapper

    def execute(self, command):
        handler = self.mapper.handler_for(command)
        return handler.execute()
