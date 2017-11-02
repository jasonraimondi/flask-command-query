import unittest

from action.tweet.get_tweet import GetTweet
from action.tweet.upvote_tweet import UpvoteTweet
from tests.lib.application_test_case import ApplicationTestCase


class UpvoteTweetHandlerTest(unittest.TestCase, ApplicationTestCase):
    def test_we_get_some_tweets(self):
        self.dispatch_command(UpvoteTweet("59ecf4bd09984200013a1156"))
        self.dispatch_command(UpvoteTweet("59ecf4bd09984200013a1156"))
        self.dispatch_command(UpvoteTweet("59ecf4bd09984200013a1156"))
        self.dispatch_command(UpvoteTweet("59ecf4bd09984200013a1156"))
        tweet = self.dispatch_command(GetTweet("59ecf4bd09984200013a1156"))

        print(tweet.text)

        self.assertTrue(tweet.votes >= 1)
