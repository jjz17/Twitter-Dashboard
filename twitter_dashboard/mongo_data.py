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

        for i, status in enumerate(tweets):
            user = status.user
            print(f"{i+1}. {user.screen_name}")
            self.collection.update_one(
                {"user": user.screen_name},
                {"$push": {"tweets": status._json}},
                upsert=True,
            )

    def load_data(
        self, users: Optional[List[str]] = None, n_tweets: Optional[int] = None
    ) -> List[Dict[str, Union[str, List[dict]]]]:
        """
        Load tweet data from the Mongo database.

        Returns:
            List[Dict[str, Union[str, List[dict]]]]: a list of dicts with user's names and respective tweets
        """
        data = []
        tweets_count = 0
        for document in self.collection.find():
            # If number of tweets requested is reached
            if n_tweets and tweets_count >= n_tweets:
                break
            if users:
                if document["user"] in users:
                    data.append(
                        {"user": document["user"], "tweets": document["tweets"]}
                    )
                    tweets_count += 1
            else:
                data.append({"user": document["user"], "tweets": document["tweets"]})
                tweets_count += 1
        return data
