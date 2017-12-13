import pydbfunction
import pylast
import parsetoptag
import re
# select SQL 
sql = "SELECT * FROM rawtable2"
db = pydbfunction.MyDBTest()    
result = db.test5(sql)     

rule=re.compile(r'[^a-zA-z0-9]')

# output
savelist = list()
for record in result:
  sn=re.sub(rule, ' ', record[1])
  artist=re.sub(rule, ' ', record[2])
  song=re.sub(rule, ' ', record[3])
  lyrics=re.sub(rule, ' ', record[5])
  mood=re.sub(rule, ' ', record[4])

  print (sn, artist, song, lyrics, mood)



  savelist.append(sn+','+artist+','+song+','+lyrics+','+mood)

##text=List of strings to be written to file
with open('stock.csv','wb') as file:
    for line in savelist:
        file.write(line)
        file.write('\n')
