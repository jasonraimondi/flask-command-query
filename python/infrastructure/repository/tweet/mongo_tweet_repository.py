from domain_model.entity.tweet import Tweet
from infrastructure.repository.tweet.tweet_repository import TweetRepositoryInterface


class MongoTweetRepositoryInterface(TweetRepositoryInterface):
    def get_by_id(self, tweet_id):
        return Tweet.objects(id=tweet_id).first()

    def count_total(self):
        return Tweet.objects.count()

    def list_by_page(self, page=0, items_per_page=1, order_by='-total_favorites'):
        start = items_per_page * page
        end = start + items_per_page
        return Tweet.objects().order_by()[start:end]

    def delete_by_id(self, tweet_id):
        tweet = self.get_by_id(tweet_id)
        tweet.delete()

    def save(self, tweet: Tweet):
        tweet.update()
