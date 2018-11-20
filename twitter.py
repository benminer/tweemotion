import tweepy

auth = tweepy.OAuthHandler('1SgQACbCCUF362ZgkZNj8NF8A', 'ltoHOdYOfgwOuPkiCEIyb6IX3gn7vBOMOM0vmWK466Kw5DJtsI')
auth.set_access_token('847301221794824192-9bwDTIRSZT59Oyf4m7YgEk0iEszwLxk',
                      'mCIEvfAV8xXRDowMxzRN2c79wLjPZbQdSMIPAweHDG7Tp')

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