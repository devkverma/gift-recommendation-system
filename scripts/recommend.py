import numpy as np
import pandas as pd
import pickle
import os
import string
import gdown
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity

stemmer = SnowballStemmer("english")
stop_words = set(stopwords.words('english'))
punctuations = string.punctuation

class Recommend:

    def __init__(self):

        base_dir = os.getcwd()
        
        data_url = "https://drive.google.com/uc?id=1Zg8J7dSM6T8ykvUpCnEFbe6iSDjaaQLE"
        vectorizer_url = "https://drive.google.com/uc?id=19F85YGfOAcBL9GuHYDiGyAdnYhimJqu8"
        vectors_url = "https://drive.google.com/uc?id=1xeEPueik57VXKw6CmDXe0hA5p7auKCCK"

        if os.path.isdir(f"{base_dir}/gift-recommendation-system/scripts/data.pkl"):
            with open(f"{base_dir}/gift-recommendation-system/scripts/data.pkl", 'rb') as file:
                self.data = pickle.load(file)
        else:
            gdown.download(data_url, f"{base_dir}/gift-recommendation-system/scripts/data.pkl", quiet=False)
            with open(f"{base_dir}/gift-recommendation-system/scripts/data.pkl", 'rb') as file:
                self.data = pickle.load(file)

        if os.path.isdir(f"{base_dir}/gift-recommendation-system/scripts/vectorizer.pkl"):
            with open(f"{base_dir}/gift-recommendation-system/scripts/vectorizer.pkl", 'rb') as file:
                self.vectorizer = pickle.load(file)
        else:
            gdown.download(vectorizer_url, f"{base_dir}/gift-recommendation-system/scripts/vectorizer.pkl", quiet=False)
            with open(f"{base_dir}/gift-recommendation-system/scripts/vectorizer.pkl", 'rb') as file:
                self.vectorizer = pickle.load(file)

        if os.path.isdir(f"{base_dir}/gift-recommendation-system/scripts/vectors.pkl"):
            with open(f"{base_dir}/gift-recommendation-system/scripts/vectors.pkl", 'rb') as file:
                self.vectors = pickle.load(file)
        else:
            gdown.download(vectors_url, f"{base_dir}/gift-recommendation-system/scripts/vectors.pkl", quiet=False)
            with open(f"{base_dir}/gift-recommendation-system/scripts/vectors.pkl", 'rb') as file:
                self.vectors = pickle.load(file)

    def __cleanText(self, text):
        tokens = word_tokenize(text)

        new_tokens = [stemmer.stem(word.lower()) for word in tokens if word not in stop_words and word not in punctuations]

        return " ".join(new_tokens)

    def recommend(self, userInput):
        userInput = self.__cleanText(userInput)
        userVector = self.vectorizer.transform([userInput])

        similarity_scores = cosine_similarity(userVector, self.vectors)

        top_n = 20
        top_n_indices = similarity_scores.argsort()[0][-top_n:][::-1] 

        products = []

        for index in top_n_indices:
            products.append(self.data.iloc[index]['ProductId'])

        return products

