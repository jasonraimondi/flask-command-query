from injector import inject

from action.tweet.get_tweet import GetTweet
from infrastructure.lib.command_handler_interface import CommandHandlerInterface
from infrastructure.repository.tweet.tweet_repository import TweetRepositoryInterface


class GetTweetHandler(CommandHandlerInterface):
    @inject
    def __init__(self, command: GetTweet, tweet_repository: TweetRepositoryInterface):
        self.command = command
        self.tweet_repository = tweet_repository

    def execute(self):
        return self.tweet_repository.get_by_id(self.command.tweet_id)
