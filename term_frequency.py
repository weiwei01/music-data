# count-list-items-1.py
import pydbfunction
import obo

def writeFile(fileName, sorteddict):
	f = open('music_exp/relaxed_term_freq_output.txt', 'a')
	f.write(fileName + "\n" + str(sorteddict) + "\n\n")
	f.close()

	print ("==========write successful==========")


# select SQL 
sql = "SELECT * FROM rawtable2"
db = pydbfunction.MyDBTest()    
result = db.test5(sql)     


wordstring = ''
for record in result:
	if record[4] == "relaxed":
		#print (record[4])
		wordstring += record[5]

text = wordstring.lower()
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

print(sorteddict.len())
#writeFile("angry_freq_remove stop word",sorteddict)
