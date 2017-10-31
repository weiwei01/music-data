#getTopTags
import pydbfunction
import pylast
import parsetoptag
# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "77e3d0a89b1d9d58d18ac1cbedab9d1f"  # this is a sample key
API_SECRET = "0dd6112837d31495ad74b8c1a1bf2181"

# In order to perform a write operation you need to authenticate yourself
username = "wi4213"
password_hash = pylast.md5("q1w@e3r4")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)


# select SQL 
sql = "SELECT * FROM rawtable2"
db = pydbfunction.MyDBTest()    
result = db.test5(sql)     

# output
for record in result:
	print (record[1], record[2], record[3])
	try:
		#get top tags
		track = network.get_track(record[2], record[3])
		toptags=track.get_top_tags()
		print(track)
		print len(toptags)
		print toptags
	except:
		print("exception!")
	track = network.get_track(record[2], record[3])
	toptags=track.get_top_tags()
	print(track)
	print len(toptags)
	print toptags
	#update sql
	update = ("""UPDATE rawtable2 SET toptags=%s WHERE indexing=%s""")
	data = (toptags, record[1])
	db = pydbfunction.MyDBTest()
	db.updateData(update, data)
	exit(0)
