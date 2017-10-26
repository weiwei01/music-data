#!/usr/bin/python3
 
import pymysql




 
# open db
db = pymysql.connect("localhost","phpmyadmin","12qwaszx","musicdb" )
 
# use cursor() 
cursor = db.cursor()
 
# SQL insert
sql = """INSERT INTO rawtable( indexing,
         artist, title, mood)
         VALUES ('Mac', 'Mohan', '20', 'M')"""
try:
   # execute sql
   cursor.execute(sql)
   # submit to db
   db.commit()
except:
   # rollback if error
   db.rollback()
 
# close db connection
db.close()
