"""
Tokenization with NLTK
------------------------
Tokenization = splitting raw text into smaller units (words, sentences).
"""

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')


text = "Natural Language Processing is amazing! It helps computers understand human language."


# ---------- 1. Word Tokenization ----------
words = word_tokenize(text)
print("Word Tokens:")
print(words)
print()


# ---------- 2. Sentence Tokenization ----------
sentences = sent_tokenize(text)
print("Sentence Tokens:")
print(sentences)


if __name__ == "__main__":
    pass
