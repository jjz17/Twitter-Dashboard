1. Improve data save and retrieval
    * Don't add duplicate tweets in `MongoStore.save_tweets_to_db` or create function to drop duplicates (by tweet id?)
    * Look into Tweepy streaming api
2. Set up application infrastructure
    * Create backend FastAPI
        * endpoint to load data from mongo
        * endpoint to extract tweets from twitter (and display in react app)
        * endpoint to save extracted tweets to mongo
    * Create frontend React
        * Multi check box on right for users to include
        * Integer input for number of tweets to load
        * Integer input and submit button to retrieve given number of tweets from timeline and save
        * List of users with tweets displayed on left (with scroll if too long)


# Resources
Tweepy API v2 Example
https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9
Snscrape Example (Scrape global tweet data)
https://python.plainenglish.io/how-to-scrape-everything-from-twitter-using-python-b91eae5e4614

https://stackoverflow.com/questions/872565/remove-sensitive-files-and-their-commits-from-git-history

# Git command to remove .env from all git history locally and in remote repo
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch twitter_dashboard/.env" \
  --prune-empty --tag-name-filter cat -- --all
  git push --force --verbose --dry-run
  git push --force
