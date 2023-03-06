import pandas as pd
import numpy as np
from numpy import argmax

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax


class SentimentAnalyzer:
    def __init__(self) -> None:
        pass

    def preprocess_text(text: str) -> str:
        pass

    def analyze_sentiment(text: str) -> int:
        pass


class RobertaModel(SentimentAnalyzer):
    def __init__(self) -> None:
        super().__init__()
        roberta = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.model = AutoModelForSequenceClassification.from_pretrained(roberta)
        self.tokenizer = AutoTokenizer.from_pretrained(roberta)

    def preprocess_text(self, text: str) -> str:
        words = []
        for word in text.split(" "):
            if word.startswith("@") and len(word) > 1:
                word = "@user"
            elif word.startswith("http"):
                word = "http"
            words.append(word)
        return " ".join(words)

    def analyze_sentiment(self, text: str) -> int:
        processed_text = self.preprocess_text(text)
        encoded_tweet = self.tokenizer(processed_text, return_tensors="pt")
        output = self.model(**encoded_tweet)

        # Convert output pytorch tensor to numpy array by detaching the computational graph
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ind = argmax(scores)
        
        return ind
