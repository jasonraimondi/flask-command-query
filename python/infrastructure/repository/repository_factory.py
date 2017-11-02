from infrastructure.repository.tweet.mongo_tweet_repository import MongoTweetRepositoryInterface
from infrastructure.repository.tweet.tweet_repository import TweetRepositoryInterface


class RepositoryFactory(object):
    def tweet_repository(self) -> TweetRepositoryInterface:
        return MongoTweetRepositoryInterface()
