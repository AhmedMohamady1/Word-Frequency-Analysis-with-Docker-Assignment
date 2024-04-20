# Read the txt file contents and initialize it into a variable
file=open(r'paragraphs.txt','r')
paragraphs=file.read()
# Close the file after we're done reading
file.close()

# Import the stopwords and word_tokenize packages from the nltk(Natural Language Kit) library
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Getting the list of Stop Words into a set variable
stop_words = set(stopwords.words('english'))
# Converting the paragraphs string into a list of word tokens
word_tokens = word_tokenize(paragraphs)

# Converting the word tokens into lowercase so we can count them properly
word_tokens_lower=[]
for w in word_tokens:
    word_tokens_lower.append(w.lower())

# Filtering the stop words from the word tokens
filtered_paragraphs=[]
for w in word_tokens_lower:
    if w not in stop_words:
        filtered_paragraphs.append(w)
        
# Importing the Counter package from the collections library
from collections import Counter

# Using the method Counter to count the frequency of each word
counts=Counter(filtered_paragraphs).most_common()
print(counts)