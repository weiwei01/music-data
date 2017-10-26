#!/usr/bin/python3
 
import pymysql
 
# open db
db = pymysql.connect("localhost","root","12qwaszx","mysql" )
 
# use cursor()
cursor = db.cursor()
 
# SQL update 
sql = "UPDATE lyricstable SET lyrics = 'test' WHERE sn = ML1"
try:
   # execute
   cursor.execute(sql)
   # commit
   db.commit()
except:
   # if error then rollback
   db.rollback()
 
# clos db connect

db.close()

