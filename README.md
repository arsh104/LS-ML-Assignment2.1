## 🔍 Key Observations

### ✅ Word Score Comparison

- **CountVectorizer** returns raw word counts.
  
- **Manual TF-IDF** and **TfidfVectorizer** both assign scores based on:
  - Word importance in a document (TF)
  - Rarity across documents (IDF)
 
-Word like **"the"** has low TF-IDF (appears in all documents → low IDF). idf helps in figuring out unique words to differentiate unique words in a document
but as like is a common word therefore it has lower IDF
## calculation
**IDF = log(N / df)**

## outputs:

## Manual TF-IDF 
| Doc | the  | sun     | is      | a       | star    | moon    | satellite | and     | are     | celestial | bodies  |
|-----|------|---------|---------|---------|---------|---------|-----------|---------|---------|-----------|---------|
| 0   | 0.0  | 0.0811  | 0.0811  | 0.0811  | 0.2197  | 0.0000  | 0.0000    | 0.0000  | 0.0000  | 0.0000    | 0.0000  |
| 1   | 0.0  | 0.0000  | 0.0811  | 0.0811  | 0.0000  | 0.0811  | 0.2197    | 0.0000  | 0.0000  | 0.0000    | 0.0000  |
| 2   | 0.0  | 0.0579  | 0.0000  | 0.0000  | 0.0000  | 0.0579  | 0.0000    | 0.1569  | 0.1569  | 0.1569    | 0.1569  |

##  Sklearn TF-IDF Vector
| Doc | and     | are     | bodies  | celestial | is      | moon    | satellite | star    | sun     | the     |
|-----|---------|---------|---------|-----------|---------|---------|-----------|---------|---------|---------|
| 0   | 0.0000  | 0.0000  | 0.0000  | 0.0000    | 1.4055  | 0.0000  | 0.0000    | 2.0986  | 1.4055  | 1.0000  |
| 1   | 0.0000  | 0.0000  | 0.0000  | 0.0000    | 1.4055  | 1.4055  | 2.0986    | 0.0000  | 0.0000  | 1.0000  |
| 2   | 2.0986  | 2.0986  | 2.0986  | 2.0986    | 0.0000  | 1.4055  | 0.0000    | 0.0000  | 1.4055  | 1.0000  |

##  Manual TF Table

| Doc |   the   |   sun   |   is    |   a     |  star   |  moon   | satellite |   and   |   are   | celestial | bodies  |
|-----|---------|---------|---------|---------|---------|---------|-----------|---------|---------|-----------|---------|
| 0   | 0.2000  | 0.2000  | 0.2000  | 0.2000  | 0.2000  | 0.0000  | 0.0000    | 0.0000  | 0.0000  | 0.0000    | 0.0000  |
| 1   | 0.2000  | 0.0000  | 0.2000  | 0.2000  | 0.0000  | 0.2000  | 0.2000    | 0.0000  | 0.0000  | 0.0000    | 0.0000  |
| 2   | 0.1429  | 0.1429  | 0.0000  | 0.0000  | 0.0000  | 0.1429  | 0.0000    | 0.1429  | 0.1429  | 0.1429    | 0.1429  |

## === Sklearn Count Vector ===
| Doc | and | are | bodies | celestial | is | moon | satellite | star | sun | the |
|-----|-----|-----|--------|-----------|----|------|-----------|------|-----|-----|
| 0   | 0   | 0   | 0      | 0         | 1  | 0    | 0         | 1    | 1   | 1   |
| 1   | 0   | 0   | 0      | 0         | 1  | 1    | 1         | 0    | 0   | 1   |
| 2   | 1   | 1   | 1      | 1         | 0  | 1    | 0         | 0    | 1   | 1   |
