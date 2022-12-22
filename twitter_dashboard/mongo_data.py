import pymongo
from pymongo import MongoClient
import tweepy

import json
from typing import List, Dict, Union, Optional


class MongoStore:
    def __init__(self, database_name: str, collection_name: str) -> None:
        self.client = MongoClient()
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def save_tweets_to_db(self, tweets: List[tweepy.models.Status]):
        """
        Save the extracted tweets to the Mongo database.
        """

        # TODO: order tweets by oldest to newest

        for i, status in enumerate(tweets):
            user = status.user
            print(f"{i+1}. {user.screen_name}")
            self.collection.update_one(
                {"user": user.screen_name},
                {"$push": {"tweets": status._json}},
                upsert=True,
            )

    def load_data(
        self,
        users: Optional[List[str]] = None,
        n_tweets: Optional[int] = None,
        n_user_tweets: Optional[int] = None,
        latest: bool = False,
    ) -> List[Dict[str, Union[str, List[dict]]]]:
        """
        Load tweet data from the Mongo database.

        Returns:
            List[Dict[str, Union[str, List[dict]]]]: a list of dicts with user's names and respective tweets
        """
        data = []
        tweets_count = 0
        for document in self.collection.find():

            user = document["user"]
            tweets = document["tweets"]

            # Skip user if not in users
            if users and user not in users:
                continue

            user_data = {"user": user, "tweets": []}
            user_tweets_count = 0

            if latest:
                tweets = tweets[::-1]

            for tweet in tweets:
                # If number of tweets requested per user or total is reached
                if (n_tweets and tweets_count >= n_tweets) or (
                    n_user_tweets and user_tweets_count >= n_user_tweets
                ):
                    break

                user_data["tweets"].append(tweet)
                tweets_count += 1
                user_tweets_count += 1

            data.append(user_data)

        return data
