from injector import inject

from action.tweet.delete_tweet import DeleteTweet
from infrastructure.lib.command_handler_interface import CommandHandlerInterface
from infrastructure.repository.tweet.tweet_repository import TweetRepositoryInterface


class DeleteTweetHandler(CommandHandlerInterface):
    @inject
    def __init__(self, command: DeleteTweet, tweet_repository: TweetRepositoryInterface):
        self.command = command
        self.tweet_repository = tweet_repository

    def execute(self):
        self.tweet_repository.delete_by_id(self.command.tweet_id)
