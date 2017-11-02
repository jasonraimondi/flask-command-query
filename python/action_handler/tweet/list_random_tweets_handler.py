from random import randint

from injector import inject

from action.tweet.list_random_tweets import ListRandomTweets
from infrastructure.lib.command_handler_interface import CommandHandlerInterface
from infrastructure.repository.tweet.tweet_repository import TweetRepositoryInterface


class ListRandomTweetsHandler(CommandHandlerInterface):
    @inject
    def __init__(self, command: ListRandomTweets, tweet_repository: TweetRepositoryInterface):
        self.command = command
        self.tweet_repository = tweet_repository

    def execute(self):
        total_tweets = self.tweet_repository.count_total()

        return self.tweet_repository.list_by_page(
            randint(0, total_tweets),
            self.command.number
        )

