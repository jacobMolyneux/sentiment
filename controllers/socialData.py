import requests
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAGiKMwEAAAAA9IOJaFNMvj3x6FaqJQnoJyZ81Rs%3D8MVGwbqXMkCedrCMgSSlCguvPXqKBKQovKm8ZjaEqMe1N1sbs2'



    


auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
api = tweepy.API(auth)

def get_tweets(term:str):
    response = api.search_tweets(term)
    tweet_data = []
    analyzer = SentimentIntensityAnalyzer()
    for tweet in response:
        tweet_data.append({
            "Date":tweet._json['created_at'],
            "User":tweet._json['user']['name'],
            "Text":tweet._json['text'],
            "Sentiment": analyzer.polarity_scores(tweet._json['text'])  
        })
    return tweet_data


