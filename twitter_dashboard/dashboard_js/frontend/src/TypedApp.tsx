import React, { useState } from "react";
import { Counter } from "./Counter";

function App() {
    const [description, setDescription] = useState("Example description")


    return (
        <div className="App">
            <input value={description} onChange={(evt) => {
                console.log(evt.target.value);
                setDescription(evt.target.value)
            }} />

            <Counter description={description} defaultCount={10}/>
        </div>
    )
}


export default App;