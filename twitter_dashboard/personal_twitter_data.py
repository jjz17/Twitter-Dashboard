import tweepy
from tweepy import OAuthHandler
from dotenv import load_dotenv

import os
import json


# Store keys and tokens for tweepy
load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_KEY_SECRET = os.getenv("CONSUMER_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


# for item in tweepy.Cursor(api.home_timeline).items(10):
#     print(item)


class TweetLoader:
    def __init__(self) -> None:
        self.api = tweepy.API(auth)
        self.tweets = []

    
    def extract_tweets(self, count: int = 100) -> None:
        """
        Extract the given number of tweets from the Twitter home timeline,
        number of tweets requested must be [1,100].

        Args:
            count (int, optional):
                number of tweets to extract, defaults to 100

        Raises:
            TypeError: if count is not an int
            ValueError: if count is not [1, 100]
        """
        if not isinstance(count, int):
            raise TypeError("Count must be an integer")
        if count < 1 or count > 100:
            raise ValueError("Count must be between 1 and 100, inclusive")

        # Extract tweets
        new_tweets = tweepy.Cursor(self.api.home_timeline).items(count)
        # Add tweets to TweetLoader storage
        self.tweets.extend(new_tweets)


    def get_loaded_tweets_as_json(self):
        """
        Return the loaded tweets as a list of JSON objects
        """
        return [tweet._json for tweet in self.tweets]