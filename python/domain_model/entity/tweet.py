from mongoengine import *
from datetime import datetime
import time


class Tweet(Document):
    id = ObjectIdField(required=True, name="_id")
    twitter_username = StringField(required=True, name="usernameTweet")
    twitter_id = StringField(required=True, name="ID")
    user_id = StringField(required=True, name="user_id")
    total_retweets = IntField(required=True, name="nbr_retweet")
    total_replies = IntField(required=True, name="nbr_reply")
    total_favorites = IntField(required=True, name="nbr_favorite")
    twitter_link = StringField(required=True, name="url")
    text = StringField(required=True, name="text")
    date_time_string = StringField(required=True, name="datetime")
    is_reply = BooleanField(required=True, name="is_reply")
    is_retweet = BooleanField(required=True, name="is_retweet")
    has_media = BooleanField(required=False)
    medias = StringField(required=False)
    votes = IntField(required=False, name="votes")
