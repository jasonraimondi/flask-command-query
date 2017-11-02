from injector import inject

from action.tweet.list_tweets import ListTweets
from infrastructure.lib.command_handler_interface import CommandHandlerInterface
from infrastructure.repository.tweet.tweet_repository import TweetRepositoryInterface


class ListTweetsHandler(CommandHandlerInterface):
    @inject
    def __init__(self, command: ListTweets, tweet_repository: TweetRepositoryInterface):
        self.command = command
        self.tweet_repository = tweet_repository

    def execute(self):
        return self.tweet_repository.list_by_page(
            self.command.page,
            self.command.items_per_page,
            self.command.order_by
        )
