import pymongo
from pymongo import MongoClient
import tweepy

import json
from typing import List, Dict, Union


class MongoStore:
    def __init__(self, database_name: str, collection_name: str) -> None:
        self.client = MongoClient()
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def save_tweets_to_db(self, tweets: List[tweepy.models.Status]):
        """
        Save the extracted tweets to the Mongo database.
        """

        for i, status in enumerate(tweets):
            user = status.user
            print(f"{i+1}. {user.screen_name}")
            self.collection.update_one(
                {"user": user.screen_name},
                {"$push": {"tweets": status._json}},
                upsert=True,
            )

    def load_data(self) -> List[Dict[str, Union[str, List[dict]]]]:
        """
        Load tweet data from the Mongo database.

        Returns:
            List[Dict[str, Union[str, List[dict]]]]: a list of dicts with user's names and respective tweets
        """
        data = []
        for document in self.collection.find():
            data.append({"user": document["user"], "tweets": document["tweets"]})
        return data
