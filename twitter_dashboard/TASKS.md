1. Set up basic data infrastructure
    * Create service to extract Twitter data (using tweepy)
    * Create service to store and retrieve data from MongoDB
2. Set up application infrastructure
    * Create backend FastAPI
        * Endpoint(s) for exacting twitter data (and storing in mongo) 
        * Endpoint(s) for extracting data from mongo
        * Endpoint for running sentiment analysis on a tweet
    * Create frontend React


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