import React, { useState } from 'react'

/*
A named export must be imported by its name in curly braces:
import {CounterProps} from ".path-to-file"
*/
export interface CounterProps {
    description: string;
    defaultCount: number;
}

/* 
A file can only have one default export
This will be imported as:
import WhateverNameYouChoose from ".path-to-file"
*/
// export default function Counter() {
//   return (
//     <div>Counter</div>
//   )
// }

export function Counter({ description, defaultCount }: CounterProps) {
    const [count, setCount] = useState(defaultCount);

    return (
        <div>
            <h5>
                DESC: {description} - DC: {defaultCount}
            </h5>

            <button onClick={() => setCount(count - 1)}>-</button>
            {count}
            <button onClick={() => setCount(count + 1)}>+</button>
        </div>
    )
}
