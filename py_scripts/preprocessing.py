import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk.stem.porter import PorterStemmer
import re
from unidecode import unidecode

# Pipeline - Text Preprocessing
def preprocessing(string, lemmatizer, stemmer, stopwords=nltk.corpus.stopwords.words('portuguese')):
    ###
    # Lowercase words
    string = string.lower()
    #Remove accents
    string = unidecode(string)
    #Remove sites
    string = re.sub(r'http\S+', '', string)
    # Remove Numbers
    string = re.sub(r'\d', '', string)
    ###
    # Remove Special Characters
    string = re.sub(r"[^a-zA-Z0-9]+", ' ', string)
    
    ###
    # Word Tokenize
    words = word_tokenize(string)
    ###
    # Remove Stopwords
    filtered_words = []
    for w in words:
        if w not in stopwords:
            filtered_words.append(w)
    #lemmatizing words
    lema_words = []
    for w in filtered_words:
        l_words = lemmatizer.lemmatize(w)
        lema_words.append(l_words)
    ###
    # Stemming Words
    stem_words = []
    for w in lema_words:
        s_words = stemmer.stem(w)
        stem_words.append(s_words)
        
    return stem_words