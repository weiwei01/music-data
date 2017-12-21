from sklearn.datasets import fetch_20newsgroups
news = fetch_20newsgroups(subset='all')


import pandas

news = pandas.read_csv("stock_half.csv", sep=",")
target = news['mood']
text = news['firstpart']

fixed_text = text[pandas.notnull(text)]
fixed_target = target[pandas.notnull(text)]

print (len(news.lyrics))
# 18846
 
print (len(news.mood))
# 20
 
print (news.mood)
# ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']
 


'''
for text, num_label in zip(news.lyrics[:10], news.mood[:10]):
    print ('[%s]:\t\t "%s ..."' % (news.mood[num_label], text[:100].split('\n')[0]))
 '''
# [rec.sport.hockey]:        "From: Mamatha Devineni Ratnam <mr47+@andrew.cmu.edu> ..."
# [comp.sys.ibm.pc.hardware]:        "From: mblawson@midway.ecn.uoknor.edu (Matthew B Lawson) ..."
# [talk.politics.mideast]:       "From: hilmi-er@dsv.su.se (Hilmi Eren) ..."
# [comp.sys.ibm.pc.hardware]:        "From: guyd@austin.ibm.com (Guy Dawson) ..."
# [comp.sys.mac.hardware]:       "From: Alexander Samuel McDiarmid <am2o+@andrew.cmu.edu> ..."
# [sci.electronics]:         "From: tell@cs.unc.edu (Stephen Tell) ..."
# [comp.sys.mac.hardware]:       "From: lpa8921@tamuts.tamu.edu (Louis Paul Adams) ..."
# [rec.sport.hockey]:        "From: dchhabra@stpl.ists.ca (Deepak Chhabra) ..."
# [rec.sport.hockey]:        "From: dchhabra@stpl.ists.ca (Deepak Chhabra) ..."
# [talk.religion.misc]:      "From: arromdee@jyusenkyou.cs.jhu.edu (Ken Arromdee) ..."
def writeFile(fileName, sorteddict):
	f = open('classifier.txt', 'a')
	f.write(fileName + "\n" + str(sorteddict) + "\n\n")
	f.close()

	print ("==========write successful==========")




from sklearn.cross_validation import train_test_split
 
def train(classifier, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
 
    classifier.fit(X_train, y_train)
    print ("Accuracy: %s" % classifier.score(X_test, y_test))
    return classifier

from sklearn import metrics
from sklearn import cross_validation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_ml import ConfusionMatrix
def crossValidation(classifier, X, y):
	predicted = cross_validation.cross_val_predict(classifier, X, y, cv=10)
	print("10-f-cv")
	print("accuracy: ",metrics.accuracy_score(y, predicted)) 
	print("recall: ",metrics.recall_score(y, predicted, average=None)) 

	pd.crosstab(y, predicted, rownames=['True'], colnames=['Predicted']).apply(lambda r: 100.0 * r/r.sum())

	conf = metrics.confusion_matrix(y, predicted)
	plt.imshow(conf, cmap='binary', interpolation='None')
	plt.show()
	cm = ConfusionMatrix(y, predicted)
	cm.print_stats()
	writeFile("classifier",cm)




from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
 
trial1 = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB()),
])
train(trial1, fixed_text, fixed_target)
# Accuracy: 0.846349745331
crossValidation(trial1, fixed_text, fixed_target)

from nltk.corpus import stopwords
 
trial2 = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words=stopwords.words('english'))),
    ('classifier', MultinomialNB()),
])
 
train(trial2, fixed_text, fixed_target)
# Accuracy: 0.877546689304
crossValidation(trial2, fixed_text, fixed_target)


trial3 = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words=stopwords.words('english'))),
    ('classifier', MultinomialNB(alpha=0.05)),
])
 
train(trial3, fixed_text, fixed_target)
# Accuracy: 0.909592529711
crossValidation(trial3, fixed_text, fixed_target)




trial4 = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words=stopwords.words('english'),
                             min_df=5)),
    ('classifier', MultinomialNB(alpha=0.05)),
])
 
train(trial4, fixed_text, fixed_target)
# Accuracy: 0.903013582343
crossValidation(trial4, fixed_text, fixed_target)



import string
from nltk.stem import PorterStemmer
from nltk import word_tokenize
 
def stemming_tokenizer(text):
    stemmer = PorterStemmer()
    return [stemmer.stem(w) for w in word_tokenize(text)]
 
trial5 = Pipeline([
    ('vectorizer', TfidfVectorizer(tokenizer=stemming_tokenizer,
                             stop_words=stopwords.words('english') + list(string.punctuation))),
    ('classifier', MultinomialNB(alpha=0.05)),
])
 
train(trial5, fixed_text, fixed_target)
# Accuracy: 0.910653650255
crossValidation(trial5, fixed_text, fixed_target)


from sklearn.svm import LinearSVC
trial6 = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words=stopwords.words('english'),
                             min_df=5)),
    ('classifier', LinearSVC()),
])

train(trial6, fixed_text, fixed_target)
# Accuracy: 0.903013582343
crossValidation(trial6, fixed_text, fixed_target)



