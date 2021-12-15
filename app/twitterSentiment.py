#import modules
import re
import numpy as np
import pandas as pd
from nltk.stem.porter import PorterStemmer

#removing pattern method
def remove_pattern(input_text,pattern):
    r= re.findall(pattern, input_text)
    for i in r:
        input_text = re.sub(i, '', input_text)
    return input_text

def dataPreprocessing(dataset):
    #removing patterns in tweets
    dataset['tweet'] = np.vectorize(remove_pattern)(dataset['tweet'],"@[\w]*")
    #removing twitter handles in tweets
    dataset['tweet'] = dataset['tweet'].str.replace("[^a-zA-Z#]"," ")
    #removing shortwords in tweets
    dataset['tweet'] = dataset['tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
    #tokenization
    tokenized_tweet = dataset['tweet'].apply(lambda x:x.split())
    #stemming
    stemmer = PorterStemmer()
    tokenized_tweet = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x])
    #combine this tweets back to combined dataset
    for i in range(len(tokenized_tweet)):
        tokenized_tweet[i] = ' '.join(tokenized_tweet[i])
    dataset['tweet'] = tokenized_tweet
    return (dataset)

def model(X_testdata):
    dataset = pd.read_csv('E:/DjangoPrograms/final/app/balanced.csv')
    tot_data = dataset.append(X_testdata,ignore_index=True)
    '''
    print(format(X_testdata.shape))
    print(format(dataset.shape))
    print(format(tot_data.shape))
    '''
    tot_data = tot_data.fillna(1)
    X= tot_data['tweet']
    y = tot_data['label']


    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = TfidfVectorizer(max_features=10000,ngram_range=(1,2))
    X = tfidf.fit_transform(X)
    X = X.toarray()
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.102, random_state=0)

    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(random_state=0)
    classifier.fit(X_train,y_train)

    y_pred = classifier.predict(X_test)
    return (y_pred)
