from sklearn import metrics
from sklearn import cross_validation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_ml import ConfusionMatrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pylab as pl
import pandas
import itertools

news = pandas.read_csv("stock_half.csv", sep=",")
target = news['mood']
text = news['secondpart']

attr_X = text[pandas.notnull(text)] #fixed_text
attr_Y = target[pandas.notnull(text)] #fixed_target
# attr_X = news['lyrics']
# attr_Y = news['mood']
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


import time
import datetime
time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
from sklearn.cross_validation import train_test_split

def train(expName, classifier, X, y):
    print (expName)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

    classifier.fit(X_train, y_train)
    print ("Accuracy: %s" % classifier.score(X_test, y_test))
    writeFile("time: ", time)

    writeFile(expName, "Accuracy: %s" % classifier.score(X_test, y_test))
    return classifier


def plot_confusion_matrix(expName, cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig(expName+"_"+time+".png")





def crossValidation(expName, classifier, X, y):
	predicted = cross_validation.cross_val_predict(classifier, X, y, cv=10)
	# print(X, y, predicted)
	# exit()
	print("10-f-cv")
	print("accuracy: ",metrics.accuracy_score(y, predicted))
	print("recall: ",metrics.recall_score(y, predicted, average=None))

	pd.crosstab(y, predicted, rownames=['True'], colnames=['Predicted']).apply(lambda r: 100.0 * r/r.sum())

	#conf = metrics.confusion_matrix(y, predicted, labels=["angry", "happy", "relaxed", "sad"])
	#plt.imshow(conf, cmap='binary', interpolation='None')
	#plt.savefig(expName+time+".png")
	#plt.show()
	labels = ['angry', 'happy', 'relaxed', 'sad']
	cm = confusion_matrix(y, predicted, labels)
	#cm.print_stats()

	# fig = plt.figure()
	# ax = fig.add_subplot(111)
	# cax = ax.matshow(cm)
	# pl.title(expName)
	# fig.colorbar(cax)
	# ax.set_xticklabels([''] + labels)
	# ax.set_yticklabels([''] + labels)
	# pl.xlabel('Predicted')
	# pl.ylabel('True')
	#pl.show()
	#pl.savefig(expName+"_"+time+".png")

	report = classification_report(y, predicted)
	print(report)

    # Compute confusion matrix
	cnf_matrix = confusion_matrix(y, predicted)
	np.set_printoptions(precision=2)

    # Plot non-normalized confusion matrix
	plt.figure()
	plot_confusion_matrix(expName, cnf_matrix, classes=labels,
                          title='Confusion matrix, without normalization')
	#plt.show()
	writeFile(expName, cm)
	writeFile(expName, report)




from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

trial1 = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB()),
])
train("Exp1", trial1, attr_X , attr_Y )
# Accuracy: 0.846349745331
crossValidation("Exp1", trial1, attr_X, attr_Y)

from nltk.corpus import stopwords

trial2 = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words=stopwords.words('english'))),
    ('classifier', MultinomialNB()),
])

train("Exp2", trial2,  attr_X, attr_Y)
# Accuracy: 0.877546689304
crossValidation("Exp2", trial2, attr_X, attr_Y)


trial3 = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words=stopwords.words('english'))),
    ('classifier', MultinomialNB(alpha=0.05)),
])

train("Exp3", trial3,  attr_X, attr_Y)
# Accuracy: 0.909592529711
crossValidation("Exp3", trial3, attr_X, attr_Y)




trial4 = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words=stopwords.words('english'),
                             min_df=5)),
    ('classifier', MultinomialNB(alpha=0.05)),
])

train("Exp4", trial4,  attr_X, attr_Y)
# Accuracy: 0.903013582343
crossValidation("Exp4", trial4, attr_X, attr_Y)



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

train("Exp5", trial5,  attr_X, attr_Y)
# Accuracy: 0.910653650255
crossValidation("Exp5", trial5, attr_X, attr_Y)


from sklearn.svm import LinearSVC
trial6 = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words=stopwords.words('english'),
                             min_df=5)),
    ('classifier', LinearSVC()),
])

train("Exp6", trial6,  attr_X, attr_Y)
# Accuracy: 0.903013582343
crossValidation("Exp6", trial6, attr_X, attr_Y)
