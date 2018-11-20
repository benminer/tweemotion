import tweepy
import os

consumer_key = os.getenv('SOOPY_TWITTER_CONSUMER_KEY')
consumer_private = os.getenv('SOOPY_TWITTER_CONSUMER_PRIVATE')
api_key = os.getenv('SOOPY_TWITTER_API_KEY')
api_secret = os.getenv('SOOPY_TWITTER_API_PRIVATE')

auth = tweepy.OAuthHandler(consumer_key, consumer_private)
auth.set_access_token(api_key, api_secret)

api = tweepy.API(auth)


def getTweets(search):
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=search, lang="en").items(100)]
    tweets = []
    for tweet in searched_tweets:
        tweets.append(tweet.text)
    return tweets


def getRateLimit():
    res = api.rate_limit_status()
    return res


getTweets('python')
