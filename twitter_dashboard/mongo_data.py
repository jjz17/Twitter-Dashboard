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
        n_tweets: Optional[int] = None,
        n_user_tweets: Optional[int] = None,
        groupby_user: bool = True,
        latest: bool = False,
    ) -> List[Dict[str, Union[str, List[dict]]]]:
        """
        Load tweet data from the Mongo database.

        Optional query parameters available

        Returns:
            List[Dict[str, Union[str, List[dict]]]]: a list of dicts with user's names and respective tweets
        """
        pipeline = []

        if users:
            # Add filter for requested users
            pipeline.append({"$match": {"user.screen_name": {"$in": users}}})

        if groupby_user:
            # Group tweets by user
            pipeline.append({"$group": {"_id": "$user.screen_name", "docs": {"$push": "$$ROOT"}}})

        # data is a list of dicts (username : list of tweets/dicts)
        data = list(self.collection.aggregate(pipeline))

        truncated_data = dict()

        # Order alphabetically by username (Mongo doesn't return in specific order)
        # NOTE: May bias users with names in earlier alphabet if n_tweets restriction is added
        if groupby_user:
            data = sorted(data, key=lambda x: x["_id"].lower())
            tweets_count = 0

            for user in data:
                # If no limit set for n_tweets:
                if not n_tweets:
                    pass
                elif tweets_count >= n_tweets:
                    break

                tweets = user["docs"]
                print(user["_id"])

                # If no limit set for n_tweets:
                if not n_tweets:
                    pass
                elif len(tweets) > n_tweets - tweets_count:
                    tweets = tweets[: n_tweets - tweets_count]

                # If there is a limit set for n_user_tweets:
                if n_user_tweets:
                    tweets = tweets[:n_user_tweets]
                    # print(group["docs"])
                    # print(len(group["docs"]))
                    print(len(tweets))

                tweets_count += len(tweets)
                # Sort tweets by most recent to least recent
                if latest:
                    tweets = tweets[::-1]
                truncated_data[user["_id"]] = tweets
        
        # If not groupby user, ignore n_user_tweets
        else:
            data = sorted(data, key=lambda x: x["user"]["screen_name"].lower())
            # Only return the number of tweets requested
            data = data[:n_tweets]

            for tweet in data:
                username = tweet["user"]["screen_name"]
                if username not in truncated_data:
                    truncated_data[username] = [tweet]
                else:
                    truncated_data[username].append(tweet)

        return truncated_data

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
