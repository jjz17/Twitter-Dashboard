import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

const url = "http://localhost:8000/load-tweets";
const url2 = "http://localhost:8000/todo";
const url3 = "http://localhost:8000/load-mongo";

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
    fetch(url3)
      .then(response => response.json())
      // .then(res => console.log(res))
      .then(res => setData(res))
      .catch(err => setError(err))
  }, [])

  console.log(data)

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
      <div>
        <ul>
          {data.map(user_data => <li key={user_data.user}>{user_data.tweets[0].text}</li>)}
        </ul>
      </div>
    </div>
  );
}

export default App;
