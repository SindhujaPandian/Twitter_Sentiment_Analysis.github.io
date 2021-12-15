from textblob import TextBlob
import tweepy
from nltk.sentiment.vader import SentimentIntensityAnalyzer

consumerKey = "kcECETl2cHMHFvcmZg00JJ7ox"
consumerSecret = "bIgz1L54uQGYFAHIZynzj4GY33cAL3spPSO6v4n6dMbOauk0RH"
accessToken = "1113114787473371136-UIFWlK19yFNw7XEQhSft1jfiHbzhce"
accessTokenSecret = "rVson5wuySWh2qejUDxtdeZQJJGmeAJdHcOCyInd3CZao"
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

def mlmodel(inp):
    noOfTweet = 100
    tweets = tweepy.Cursor(api.search, q=inp).items(noOfTweet)
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    tweet_list = []
    for tweet in tweets:
        tweet_list.append(tweet.text)
        analysis = TextBlob(tweet.text)
        score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        comp = score['compound']
        polarity += analysis.sentiment.polarity
    
        if neg > pos:
            negative += 1
        
        elif pos > neg:
            positive += 1

        elif pos == neg:
            neutral += 1


    print(positive)
    print(negative)
    print(neutral)

    if(positive>negative):
        if(positive>neutral):
            return("POSITIVE")
        else:
            return("NEUTRAL")
    elif(negative>neutral):
        return("NEGATIVE")
    else:
        return("NEUTRAL")