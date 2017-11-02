from injector import inject

from action.tweet.upvote_tweet import UpvoteTweet
from infrastructure.lib.command_handler_interface import CommandHandlerInterface
from infrastructure.repository.tweet.tweet_repository import TweetRepositoryInterface


class UpvoteTweetHandler(CommandHandlerInterface):
    @inject
    def __init__(self, command: UpvoteTweet, tweet_repository: TweetRepositoryInterface):
        self.command = command
        self.tweet_repository = tweet_repository

    def execute(self):
        tweet = self.tweet_repository.get_by_id(self.command.tweet_id)

        if tweet.votes is None:
            tweet.votes = 1
        else:
            tweet.votes += 1

        self.tweet_repository.save(tweet)
