from flask import Flask, render_template, redirect, url_for, request
from mongoengine import connect

from action.tweet.delete_tweet import DeleteTweet
from action.tweet.list_random_tweets import ListRandomTweets
from infrastructure.lib.application_core import ApplicationCore

app = Flask(__name__)
application_core = ApplicationCore()
connect("TweetScraper", host="mongo", port=27017)


@app.route("/")
def random_tweet():
    list_random_tweets_command = ListRandomTweets(1)
    tweets = application_core.dispatch_command(list_random_tweets_command)
    return render_template("tweets_list.html", tweets=tweets)


@app.route("/delete", methods=["POST"])
def delete_tweet():
    tweet_id = request.form["tweet_id"]
    delete_tweet_command = DeleteTweet(tweet_id=tweet_id)
    application_core.dispatch_command(delete_tweet_command)
    return redirect(url_for("random_tweet"))

