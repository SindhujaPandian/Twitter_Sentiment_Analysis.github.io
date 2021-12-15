from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from app.twitterSentiment import model

ACCESS_TOKEN = "1113114787473371136-UIFWlK19yFNw7XEQhSft1jfiHbzhce"
ACCESS_TOKEN_SECRET = "rVson5wuySWh2qejUDxtdeZQJJGmeAJdHcOCyInd3CZao"
CONSUMER_KEY = "kcECETl2cHMHFvcmZg00JJ7ox"
CONSUMER_SECRET = "bIgz1L54uQGYFAHIZynzj4GY33cAL3spPSO6v4n6dMbOauk0RH"
import pandas as pd
import numpy as np
import re
from nltk.stem.porter import PorterStemmer

class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user
    def get_twitter_client_api(self):
        return self.twitter_client
    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth

class TweetAnalyzer():
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet'])
        return df

#removing pattern method

def mlmodel(inp):
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    api = twitter_client.get_twitter_client_api()
    #inp=input('INPUT : ')
    tweets = api.search(inp,count=500)

    X_testdata = tweet_analyzer.tweets_to_data_frame(tweets)
    #print(X_testdata)
    y_pred = model(X_testdata)

    positive_weight,negative_weight = 0,0
    for i in y_pred:
        #print(i)
        if(i==1):
            positive_weight+=1
        else:
            negative_weight+=1
    #print("(positive,negative)",positive_weight,negative_weight)
    weightage_difference = positive_weight-negative_weight
    if(weightage_difference==0):
        return "NEUTRAL"
    elif(weightage_difference>0):
        return "POSITIVE"
    else:
        return "NEGATIVE"
