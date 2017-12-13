#lastfmtest

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



#get top tags
track = network.get_track("Adele", "Hello")
ttt=track.get_top_tags()
# aaa= track.get_similar()
print(track)
# print len(ttt)
# print ttt
# print len(aaa)

# print aaa
wikisummary = track.get_wiki_summary()
wikicontent = track.get_wiki_content()
print(wikisummary)
print(wikicontent)

#f = open('ml_raw.csv', 'r')
#newFile = open('newFile', 'a')
#for row in csv.reader(f):
#    print row
#f.close()