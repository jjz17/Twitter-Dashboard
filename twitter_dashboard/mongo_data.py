import pymongo
from pymongo import MongoClient
import tweepy
from datetime import datetime

import json
from typing import List, Dict, Union, Optional

"""
Mongo Collection Schema Design:

A flat collection of Tweet Status/JSON objects, uniquely indexed by object (document) ID and tweet ID
"""


class MongoTweetStore:
    def __init__(self, database_name: str, collection_name: str) -> None:
        self.client = MongoClient()
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]
        self.collection.create_index(
            [("id", pymongo.ASCENDING)],
            name="tweet_id",
            unique=True,
            default_language="english",
        )

    def save_tweets_to_db(self, tweets: List[tweepy.models.Status]):
        """
        Save the extracted tweets to the Mongo database.
        """

        # Order tweets by oldest to newest
        tweets = sorted(tweets, key=lambda x: x.created_at)

        for i, tweet in enumerate(tweets):
            try:
                user = tweet.user
                print(f"{i+1}. {user.screen_name}")
                self.collection.insert_one(tweet._json)
            except pymongo.errors.DuplicateKeyError:
                print(f"Duplicate tweet id: {tweet.id}")

    def load_flat_data(self):
        """
        Load all documents (tweets) as a list from Mongo
        """
        data = []
        for document in self.collection.find():
            data.append(document)
        return data

    def load_data_test(
        self,
        users: Optional[List[str]] = None,
        n_tweets: int = 0,
        n_user_tweets: int = 0,
        latest: bool = False,
    ) -> List[Dict[str, Union[str, List[dict]]]]:
        """
        Load tweet data from the Mongo database.

        Optional query parameters available

        Returns:
            List[Dict[str, Union[str, List[dict]]]]: a list of dicts with user's names and respective tweets
        """
        pipeline = [
            # Group tweets by user
            {
                "$group": {"_id": "$user.screen_name", "docs": {"$push": "$$ROOT"}},
            },
        ]

        if users:
            # Add filter for requested users
            pipeline.insert(0, {"$match": {"user.screen_name": {"$in": users}}})

        # data is a list of dicts (username : list of tweets/dicts)
        data = self.collection.aggregate(pipeline)

        # Order alphabetically by username (Mongo doesn't return in specific order)
        data = sorted(data, key=lambda x: x["_id"].lower())

        tweets_count = 0
        for group in data:
            if tweets_count >= n_tweets:
                break

            tweets = group["docs"]
            print(group["_id"])

            if len(tweets) > n_tweets - tweets_count:
                tweets = tweets[: n_tweets - tweets_count]

            if n_user_tweets:
                tweets = tweets[:n_user_tweets]
                # print(group["docs"])
                # print(len(group["docs"]))
                print(len(tweets))

            tweets_count += len(tweets)

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


if __name__ == "__main__":
    store = MongoTweetStore("twitter_dashboard_db", "home_timeline")
    data = store.load_data_test(users=["business", "Forbes"], n_tweets=100, n_user_tweets=100)
