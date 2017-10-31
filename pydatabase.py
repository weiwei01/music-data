#!/usr/bin/python3
 
import pymysql
 
# open db connect
db = pymysql.connect("localhost","phpmyadmin","12qwaszx","musicdb" )
 
# use cursor() method to create an object
cursor = db.cursor()
 
# use execute() method ot query SQL  
cursor.execute("SELECT VERSION()")
 
# use fetchone() method to fetch one record
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# close db connect
db.close()

