import nlpcloud
import requests
from transformers import pipeline
import torch
class API:
    def __init__(self):
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        self.ner_tagger = pipeline("ner", grouped_entities=True)
        self.emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")
    
    def sentiment_analysis(self, text):
        try:
            result = self.sentiment_analyzer(text)
            return {"sentiment": result}
        except Exception as e:
            return {"error": str(e)}
        
    def ner(self, text):
        try:
            result = self.ner_tagger(text)
            return {"entities": result}
        except Exception as e:
            return {"error": str(e)}

    def emotion(self, text):
        try:
            result = self.emotion_classifier(text)
            return {"emotions": result}
        except Exception as e:
            return {"error": str(e)}
