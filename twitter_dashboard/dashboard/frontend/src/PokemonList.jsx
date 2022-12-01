import React from 'react'

export default function PokemonList({ pokemon }) {
  return (
    // Iterate/map over each element in the pokemon list and render it in a div
    <div>
      {pokemon.map(p => (
        <div key={p}>{p}</div>
      ))}
    </div>
  )
}