import requests
import tweepy



auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
api = tweepy.API(auth)

def get_tweets(term:str):
    response = api.search_tweets(term)
    tweet_data = []
    for tweet in response:
        tweet_data.append({
            "Text":tweet._json['text'],
            "Date":tweet._json['created_at'],
            "User":tweet._json['user']['name']
        })
    return tweet_data


