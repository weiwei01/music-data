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

# Now you can use that object everywhere
artist = network.get_artist("System of a Down")
print(artist)
#artist.shout("<3")


track = network.get_track("Usher", "There Goes My Baby")
track.love()
track.add_tags(("awesome", "favorite"))

lastfm_artist = network.get_artist("Metallica")
tags = lastfm_artist.get_top_tags()

print len(tags)
print tags

ttt=track.get_top_tags()
print(track)
print len(ttt)
print ttt
# Type help(pylast.LastFMNetwork) or help(pylast) in a Python interpreter
# to get more help about anything and see examples of how it works
