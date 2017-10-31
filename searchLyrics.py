import pydbfunction
import lyricwikia
# select SQL 
sql = "SELECT * FROM rawtable2 where lyric = ''"
db = pydbfunction.MyDBTest()    
result = db.test5(sql)     

# output
for record in result:
	print (record[1], record[2], record[3])
	try:
		lyrics = lyricwikia.get_lyrics(record[2], record[3])
		print(lyrics)
		#update sql
		update = ("""UPDATE rawtable2 SET lyric=%s WHERE indexing=%s""")
		data = (lyrics, record[1])
		db = pydbfunction.MyDBTest()
		db.updateData(update, data)
	except:
		print("exception!")










