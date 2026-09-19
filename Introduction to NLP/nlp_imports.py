"""
NLP Starter Imports
--------------------
Common libraries used for Natural Language Processing projects.
Install missing ones with: pip install nltk spacy scikit-learn gensim pandas numpy
"""

# ---------- Core Python ----------
import re
import string

# ---------- NLTK (Natural Language Toolkit) ----------
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required NLTK data (only needs to run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# ---------- spaCy ----------
import spacy
# Load English model (install first: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# ---------- Scikit-learn (classical ML for NLP) ----------
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ---------- Gensim (topic modeling, Word2Vec) ----------
import gensim
from gensim.models import Word2Vec

# ---------- Data handling ----------
import pandas as pd
import numpy as np

# ---------- Hugging Face Transformers (modern NLP) ----------
from transformers import pipeline, AutoTokenizer, AutoModel


if __name__ == "__main__":
    print("All NLP libraries imported successfully.")
