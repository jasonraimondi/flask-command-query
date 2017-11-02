from infrastructure.lib.command_interface import CommandInterface


class ListTweets(CommandInterface):
    def __init__(self, page: int = 0, items_per_page: int = 1, order_by: str = '-total_favorites'):
        self.order_by = order_by
        self.page = page
        self.items_per_page = items_per_page
