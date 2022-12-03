import React, { useEffect, useState } from "react";

function App() {
    const [tweet, setTweet] = useState("First tweet")


    return (
        <div className="App">
            <input onChange={(evt) => {
                console.log(evt.target.value);
            }} />
        </div>
    )
}



export default App;