import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
# Must do initial download
#import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

sentenses = [
    'The river is frozen'
    ,'The river is blue'
    ,'The sun is burning'
    ,'The sun is yellow'
]

def clean_string(text):
    text = ''. join([word for word in text if word not in string.punctuation])
    text = text.lower()
    text = ' '. join([word for word in text.split() if word not in stop_words])
    return text

cleaned = list(map(clean_string, sentenses))
vectorizer = CountVectorizer().fit_transform(cleaned)
vectors = vectorizer.toarray()
print(vectors)

csim = cosine_similarity(vectors)
print(csim)

def cosine_sim_vectors(vec1, vec2):
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1, -1)
    return cosine_similarity(vec1, vec2)[0][0]

#test
test = cosine_sim_vectors(vectors[0], vectors[1])
print(test)