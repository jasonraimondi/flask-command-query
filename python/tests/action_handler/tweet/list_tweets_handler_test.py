import unittest

from action.tweet.list_tweets import ListTweets
from tests.lib.application_test_case import ApplicationTestCase


class ListTweetsHandlerTest(unittest.TestCase, ApplicationTestCase):
    def test_we_get_some_tweets(self):
        count = 5
        page = 0

        command = ListTweets(page, count)
        tweets = self.dispatch_command(command)

        tweets_count = sum(1 for x in tweets)
        self.assertEqual(tweets_count, count)
