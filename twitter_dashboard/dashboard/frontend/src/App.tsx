import React, { useState, useEffect } from 'react';
import './App.css';

const extract_url = "http://localhost:8000/extract-tweets";
const mongo_url = "http://localhost:8000/mongo-tweets";

function App() {
  const [todos, setTodos] = useState<Todo[]>([])
  const [data, setData] = useState<any[]>([])
  const [error, setError] = useState({})

  interface Todo {
    id: string;
    item: string;
  }

  useEffect(() => {
    // fetch('https://jsonplaceholder.typicode.com/todos')
    fetch(mongo_url)
      .then(response => response.json())
      // .then(res => console.log(res))
      .then(res => setData(res))
      .catch(err => setError(err))
  }, [])

  // console.log(data)
  data.map(user_data => {
    console.log(user_data.user)
    user_data.tweets.map((tweet: any) => {
      console.log(tweet.text)
    });
  })

  return (
    <div className="App">
      <div>
        Hello
      </div>
      <div>
        <ul>
          <>
            {data.map(user_data => {
              user_data.tweets.map((tweet: any) => {
                <li>tweet.text</li>
              });
            })}
            {data.map(user_data => {
              return (
                <>
                  <h4>User : {user_data.user}</h4>
                  {user_data.tweets.map((tweet: any) => {
                    return (
                      <li>{tweet}</li>
                    )
                  })}
                </>
              );
            })}
          </>
        </ul>
      </div>
    </div>
  );
}

export default App;
