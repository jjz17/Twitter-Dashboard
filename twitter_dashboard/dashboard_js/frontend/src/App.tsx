import React, { useState, useEffect } from 'react';
import { ChakraProvider } from "@chakra-ui/react";

import Tweets from "./components/Tweets";
import PokemonList from './PokemonList'
import axios from 'axios'
import Pagination from './Pagination';

function App() {
  const [pokemon, setPokemon] = useState([])
  const [currentPageUrl, setCurrentPageUrl] = useState("https://pokeapi.co/api/v2/pokemon")
  const [nextPageUrl, setNextPageUrl] = useState<string>("")
  const [prevPageUrl, setPrevPageUrl] = useState<string>("")
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    setLoading(true)
    let cancel: any;
    axios.get(currentPageUrl, {
      cancelToken: new axios.CancelToken(c => cancel = c)
    }).then(res => {
      setLoading(false)
      setNextPageUrl(res.data.next)
      setPrevPageUrl(res.data.previous)
      setPokemon(res.data.results.map((p: any) => p.name))
    })

    return () => cancel()
  }, [currentPageUrl])

  function gotoNextPage() {
    setCurrentPageUrl(nextPageUrl)
  }

  function gotoPrevPage() {
    setCurrentPageUrl(prevPageUrl)
  }

  if (loading) return "Loading..."

  return (
    <>
    <ChakraProvider>
      <Tweets />
      <PokemonList pokemon={pokemon} />
      <Pagination
        gotoNextPage={nextPageUrl ? gotoNextPage : null}
        gotoPrevPage={prevPageUrl ? gotoPrevPage : null}
      />
    </ChakraProvider>
    </>
  );
}

export default App;