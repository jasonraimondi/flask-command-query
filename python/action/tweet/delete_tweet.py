from infrastructure.lib.command_interface import CommandInterface


class DeleteTweet(CommandInterface):
    def __init__(self, tweet_id: str):
        self.tweet_id = tweet_id
