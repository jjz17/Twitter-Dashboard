const extract_url = "http://localhost:8000/extract-tweets";
const mongo_url = "http://localhost:8000/mongo-tweets?n_tweets=10";

// export const getTweets = async () => {
//     const res = await fetch(mongo_url);
//     const tweets = await res.json();
//     console.log(tweets)
//     return tweets;
//   };

  export const getTweets = () => {
    return fetch(mongo_url).then((res) => res.json());
  };