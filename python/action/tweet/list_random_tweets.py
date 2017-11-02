from infrastructure.lib.command_interface import CommandInterface


class ListRandomTweets(CommandInterface):
    def __init__(self, number: int = 1):
        self.number = number
