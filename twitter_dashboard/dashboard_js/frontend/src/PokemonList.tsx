import React from 'react'

export default function PokemonList({ pokemon }: { pokemon: any }) {
  return (
    // Iterate/map over each element in the pokemon list and render it in a div
    <div>
      {pokemon.map((p: any) => (
        <div key={p}>{p}</div>
      ))}
    </div>
  )
}