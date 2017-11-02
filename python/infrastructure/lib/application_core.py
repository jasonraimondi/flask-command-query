from mongoengine import *

from infrastructure.lib.bus import Bus
from infrastructure.lib.command_interface import CommandInterface
from infrastructure.lib.mapper import Mapper
from infrastructure.repository.repository_factory import RepositoryFactory

class ApplicationCore(object):
    def dispatch_command(self, command: CommandInterface):
        return self.get_bus().execute(command)

    def get_bus(self) -> Bus:
        return Bus(self.get_mapper())

    def get_mapper(self) -> Mapper:
        return Mapper(self.get_repository_factory())

    def get_repository_factory(self) -> RepositoryFactory:
        return RepositoryFactory()
