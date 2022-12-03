import React, { useEffect, useState } from "react";
import {
    Box,
    Button,
    Flex,
    Input,
    InputGroup,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    Stack,
    Text,
    useDisclosure
} from "@chakra-ui/react";

const TweetsContext = React.createContext({
    tweets: [], fetchTweets: () => { }
})

function AddTweet() {
    const [text, setItem] = React.useState("")
    const { tweets, fetchTweets } = React.useContext(TweetsContext)

    const handleInput = (evt: any) => {
        setItem(evt.target.value)
    }

    const handleSubmit = (evt: any) => {
        const newTweet = {
            "id": tweets.length + 1,
            "text": text
        }

        fetch("http://localhost:8000/tweet", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(newTweet)
        }).then(fetchTweets)
    }

    return (
        <form onSubmit={handleSubmit}>
            <InputGroup size="md">
                <Input
                    pr="4.5rem"
                    type="text"
                    placeholder="Add a tweet"
                    aria-label="Add a tweet"
                    onChange={handleInput}
                />
            </InputGroup>
        </form>
    )
}

function UpdateTweet({text, id}: { text: string, id: number }) {
    const { isOpen, onOpen, onClose } = useDisclosure()
    const [tweet, setTweet] = useState(text)
    const { fetchTweets } = React.useContext(TweetsContext)

    const updateTweet = async () => {
        await fetch(`http://localhost:8000/tweet/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: tweet })
        })
        onClose()
        await fetchTweets()
    }

    return (
        <>
            <Button h="1.5rem" size="sm" onClick={onOpen}>Update Tweet</Button>
            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <ModalContent>
                    <ModalHeader>Update Tweet</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>
                        <InputGroup size="md">
                            <Input
                                pr="4.5rem"
                                type="text"
                                placeholder="Add a tweet"
                                aria-label="Add a tweet"
                                value={tweet}
                                onChange={e => setTweet(e.target.value)}
                            />
                        </InputGroup>
                    </ModalBody>

                    <ModalFooter>
                        <Button h="1.5rem" size="sm" onClick={updateTweet}>Update Tweet</Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </>
    )
}


function DeleteTweet({ id }) {
    const { fetchTweets } = React.useContext(TweetsContext)

    const deleteTweet = async () => {
        await fetch(`http://localhost:8000/tweet/${id}`, {
            method: "DELETE",
            headers: { "Content-Type": "application/json" },
            body: { "id": id }
        })
        await fetchTweets()
    }

    return (
        <Button h="1.5rem" size="sm" onClick={deleteTweet}>Delete Tweet</Button>
    )
}


function TweetHelper({ text, id, fetchTweets }) {
    return (
        <Box p={1} shadow="sm">
            <Flex justify="space-between">
                <Text mt={4} as="div">
                    {text}
                    <Flex align="end">
                        <UpdateTweet text={text} id={id} fetchTweets={fetchTweets} />
                        <DeleteTweet id={id} fetchTweets={fetchTweets} />  {/* new */}
                    </Flex>
                </Text>
            </Flex>
        </Box>
    )
}

interface Location {
    long: number;
    lat: number;
    /**
     * Description for altitude field
     */
    altitude: number | undefined;
}

interface TweetProps {
    id: number;
    text: string;
    location: Location
}


export default function Tweets() {
    const [tweets, setTweets] = useState([])
    const fetchTweets = async () => {
        const response = await fetch("http://localhost:8000/load-tweets")
        const tweets = await response.json()
        setTweets(tweets.data)
    }
    useEffect(() => {
        fetchTweets()
    }, [])
    return (
        <TweetsContext.Provider value={{ tweets, fetchTweets }}>
            <AddTweet />
            <Stack spacing={5}>
                {
                    tweets.map((tweet) => (
                        <TweetHelper text={tweet.text} id={tweet.id} fetchTweets={fetchTweets} />
                    ))
                }
            </Stack>
        </TweetsContext.Provider>
    )
}