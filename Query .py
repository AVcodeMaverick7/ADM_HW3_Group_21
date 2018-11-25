
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
import csv
import json
import string
import unicodedata
import re
import geopy
import geopy.distance
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from scipy.spatial.distance import cosine
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import pandas as pd


# In[3]:

def stem_sentences(sentence):
    from nltk.stem import PorterStemmer
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.stem.snowball import SnowballStemmer
    stemmer = SnowballStemmer("english")
    ps = PorterStemmer()
    tokens = sentence.split()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)


# In[4]:

o=string.punctuation+'“–'
def remove_punctuations(text):
    for punctuation in o:
        text = text.replace(punctuation, '')
    return text


# In[5]:

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])




