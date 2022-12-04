import React from 'react';
import logo from './logo.svg';
import './App.css';

// type JSONValue =
async function loadTweets() {
  const url = "http://localhost:8000/load-tweets";
  const response = await fetch(url);
  let data = ""
  if (response.ok) {
    data = await response.text()
  }
  else {
    console.log("Error HTTP: " + response.status) 
  }
  
  const tweets = JSON.parse(data)
  return tweets
}

const tweets = loadTweets();
console.log(tweets)

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      {/* <div>
        {tweets.map(tweet => <h3></h3>)}
      </div> */}
    </div>
  );
}

export default App;
