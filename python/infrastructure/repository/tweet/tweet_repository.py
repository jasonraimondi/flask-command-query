from domain_model.entity.tweet import Tweet


class TweetRepositoryInterface(object):
    def get_by_id(self, tweet_id) -> Tweet:
        raise NotImplementedError

    def count_total(self):
        raise NotImplementedError

    def list_by_page(self, page=0, items_per_page=1, order_by='-total_favorites'):
        raise NotImplementedError

    def delete_by_id(self, tweet_id):
        raise NotImplementedError

    def save(self, tweet: Tweet):
        raise NotImplementedError
