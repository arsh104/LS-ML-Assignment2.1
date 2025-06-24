"""
Manual TF-IDF implementation vs sklearn's TfidfVectorizer

This script compares manually calculated TF-IDF with the output of 
CountVectorizer and TfidfVectorizer from sklearn.

Author: [Your Name]
"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import re
import math
import pandas as pd

# Corpus
corpus = [
    'the sun is a star',
    'the moon is a satellite',
    'the sun and moon are celestial bodies'
]

# === Sklearn CountVectorizer ===
vector = CountVectorizer()
X = vector.fit_transform(corpus)
countvector = X.toarray()

# === Sklearn TfidfVectorizer ===
vector2 = TfidfVectorizer(norm=None, smooth_idf=False, use_idf=True)
Y = vector2.fit_transform(corpus)
tfidfvector = Y.toarray()

# === Manual Preprocessing ===
# Get all unique words
all_words = []
for c in corpus:
    words = re.findall(r'\b\w+\b', c.lower())  # extract words and lowercase
    all_words.extend(words)

unique = []
for x in all_words:
    if x not in unique:
        unique.append(x)

# === Manual Count Matrix ===
wordfreq = []
for i in corpus:
    words = re.findall(r'\b\w+\b', i.lower())
    li = []
    count = 0
    for word in unique:
        for w in words:
            if word == w:
                count += 1
        li.append(count)
        count = 0
    wordfreq.append(li)

# === Convert to DataFrame ===
df = pd.DataFrame(wordfreq, columns=unique)

# === Manual TF Calculation ===
tf = df.apply(lambda row: row / row.sum(), axis=1)

# === Manual IDF Calculation ===
N = len(corpus)
idf_values = []

for word in unique:
    doc_count = 0
    for sentence in corpus:
        if re.search(rf'\b{word}\b', sentence, re.IGNORECASE):
            doc_count += 1
    idf = math.log(N / (doc_count))  # IDF formula
    idf_values.append(idf)

df_idf = pd.DataFrame([idf_values], columns=unique)

# === Manual TF-IDF Calculation ===
tfidf = tf.multiply(idf_values, axis=1)

# === Display Results ===
print("=== Manual IDF ===")
print(df_idf)

print("\n=== Manual TF-IDF ===")
print(tfidf)

print("\n=== Sklearn TF-IDF Vector ===")
print(pd.DataFrame(tfidfvector,columns=vector.get_feature_names_out()))

print("\n=== Manual TF ===")
print(tf)

print("\n=== Sklearn Count Vector ===")
print(pd.DataFrame(countvector,columns=vector.get_feature_names_out()))
