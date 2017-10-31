import csv
import string
#m = l.translate(None, string.punctuation)
<<<<<<< HEAD
import pydbfunction


import sys # regular module
sys.path.append("genius")
 
import api
=======
import lyricwikia
>>>>>>> 5373fd3112ea3dc2de31573a97005d3612c479ff




<<<<<<< HEAD


with open('data/ml_raw_download.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['Index'], row['Artist'], row['Title'], row['Mood'])
         artist = row['Artist']
         title = row['Title']	
	 try:
	   G = api.Genius() 
           song = G.search_song(row['Title'], row['Artist'])
	   if song is None:
	     continue
           else:
             lyrics = song.lyrics.replace('\n','\n    ')
	   #update sql
           update = ("""UPDATE rawtable2 SET lyric=%s WHERE indexing=%s""")
           data = (lyrics, row['Index'])
           db = pydbfunction.MyDBTest()
           db.updateData(update, data)
         except:
           print("exception!")
		
   
=======
with open('data/ml_raw.csv', encoding = 'utf8') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['Index'])
         print(row['Artist'], row['Title'])
         artist = row['Artist']
         title = row['Title']
		 
         lyrics = lyricwikia.get_lyrics(artist, title)
         print(lyrics)
		 
         continue

print(123)
>>>>>>> 5373fd3112ea3dc2de31573a97005d3612c479ff

'''

'''

'''
import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "77e3d0a89b1d9d58d18ac1cbedab9d1f"  # this is a sample key
API_SECRET = "0dd6112837d31495ad74b8c1a1bf2181"

# In order to perform a write operation you need to authenticate yourself
username = "wi4213"
password_hash = pylast.md5("q1w@e3r4")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)


'''
#get top tags
track = network.get_track("Usher", "There Goes My Baby")
ttt=track.get_top_tags()
print(track)
<<<<<<< HEAD
print len(ttt)
print ttt
'''
=======
print (len(ttt))
print (ttt)

>>>>>>> 5373fd3112ea3dc2de31573a97005d3612c479ff

#f = open('ml_raw.csv', 'r')
#newFile = open('newFile', 'a')
#for row in csv.reader(f):
#    print row
#f.close()
'''


