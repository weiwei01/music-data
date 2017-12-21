import pylast
import csv
# select SQL 
f = open('stock.csv', 'r')
savelist = list()
savelist.append("sn"+','+"artist"+','+"song"+','+"lyrics"+','+"mood"+','+"firstpart"+','+"secondpart")
for row in csv.DictReader(f):
  sn=row['sn'] 
  artist=row['artist'] 
  song=row['song'] 
  lyrics=row['lyrics'] 
  mood=row['mood'] 

  #print (sn, artist, song, lyrics, mood)




  firstpart, secondpart = lyrics[:len(lyrics)//2], lyrics[len(lyrics)//2:]  
  # print("firstpart: ",str(firstpart))
  #print("secondpart: ",secondpart)

  savelist.append(sn+','+artist+','+song+','+lyrics+','+mood+','+firstpart+','+secondpart)
f.close()
##text=List of strings to be written to file
with open('stock_half.csv','wb') as file:
    for line in savelist:
        file.write(line.encode("utf-8"))
        file.write('\n'.encode("utf-8"))
