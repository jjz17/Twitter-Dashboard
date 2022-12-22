# pip3 install snscrape
# If you want to use the development version:
# pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git

import snscrape.modules.twitter as twitter

maxTweets = 10
keyword = "tb2"
for i, tweet in enumerate(
    twitter.TwitterSearchScraper(
        keyword + ' since:2021-11-01 until:2023-01-01 lang:"en" '
    ).get_items()
):
    tweets = {
        "Tweet": "Reply",
        "tweet/reply id": "a" + str(tweet.id),
        "inReplyToTweetId": "a" + str(tweet.inReplyToTweetId),
        "conversationId": "a" + str(tweet.conversationId),
        "tweet.username": tweet.username,
        "tweet.content": tweet.content,
        "tweet.date": tweet.date,
        "tweet.user.location": tweet.user.location,
        "tweet.likeCount": tweet.likeCount,
        "tweet.replyCount": tweet.replyCount,
        "tweet.retweetCount": tweet.retweetCount,
        "tweet.user.followersCount": tweet.user.followersCount,
        "tweet.user.description": tweet.user.description,
        "tweet.user.friendsCount": tweet.user.friendsCount,
        "tweet.user.statusesCount": tweet.user.statusesCount,
        "tweet.user.favouritesCount": tweet.user.favouritesCount,
        "tweet.user.listedCount": tweet.user.listedCount,
        "tweet.user.mediaCount": tweet.user.mediaCount,
        "tweet.url": tweet.url,
    }
    print(tweets)

    maxTweets = 100


def exactPhrase(keyword=""):
    for i, tweet in enumerate(
        twitter.TwitterSearchScraper(
            keyword + " since:2020-11-01 until:2021-01-01 "
        ).get_items()
    ):
        if i > maxTweets:
            break
        print(i)
        print(tweet.username)
        print(tweet.content)
        print(tweet.url)
        print("\n")


exactPhrase('"python%20learning"')


def anyOfWords(keyword=""):
    for i, tweet in enumerate(
        twitter.TwitterSearchScraper(
            keyword + " since:2020-11-01 until:2021-01-01 "
        ).get_items()
    ):
        if i > maxTweets:
            break
        print(i)
        print(tweet.username)
        print(tweet.content)
        print(tweet.url)
        print("\n")


anyOfWords("(python%20OR%20learning)")


def userTweets(username=""):
    for i, tweet in enumerate(
        twitter.TwitterSearchScraper(
            "from:" + username + ' since:2020-11-01 until:2021-01-01 lang:"en" '
        ).get_items()
    ):
        if i > maxTweets:
            break
        print(i)
        print(tweet.username)
        print(tweet.content)
        print(tweet.date)
        print(tweet.url)
        print("\n")


userTweets("Projects_007")


for i, tweet in enumerate(
    twitter.TwitterSearchScraper(
        "from:Projects_007  lang:tr since:2020-01-01 until:2020-12-30"
    ).get_items()
):
    if i > 1:
        break
    print(tweet.username)
    print(tweet.date)
    print(tweet.content)
    print(tweet.url)
    print("\n")


for i, tweet in enumerate(
    twitter.TwitterSearchScraper(
        "from:Projects_007  to:@mertcobanov lang:tr since:2020-01-01 until:2020-12-30"
    ).get_items()
):
    if i > 1:
        break
    print(tweet.username)
    print(tweet.date)
    print(tweet.content)
    print(tweet.url)
    print("\n")


for i, tweet in enumerate(
    twitter.TwitterSearchScraper(
        " geocode:37.7764685,-122.4172004,10km since:2020-01-01 until:2020-12-30"
    ).get_items()
):
    if i > maxTweets:
        break
    print(tweet.username)
    print(tweet.date)
    print(tweet.content)
    print("\n")


for i, tweet in enumerate(
    sntwitter.TwitterSearchScraper(
        " conversation_id:1425083028695658504 (filter:safe OR -filter:safe) "
    ).get_items()
):
    print(tweet)
    print(i)


keyword = "Python"
username = "Projects_007"

with open("Projects_007.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(
            "from:" + username + ' since:2020-11-01 until:2021-01-01 lang:"en" '
        ).get_items()
    ):
        writer.writerow(
            [
                tweet.username,
                tweet.content.encode("utf-8"),
                tweet.date,
                tweet.user.location,
                tweet.likeCount,
                tweet.retweetCount,
                tweet.user.followersCount,
                tweet.url,
            ]
        )
