import sys

import pymysql

class MyDBTest():

    def __init__(self):
        try:
            self.con = pymysql.connect("localhost","phpmyadmin","12qwaszx","musicdb" )
            self.cur = self.con.cursor()
	    #self.show_version()
        except :
            print "Connection Error"
            sys.exit(1)

    def show_version(self):
            self.cur.execute("SELECT VERSION()")
            print "Database version : %s " % self.cur.fetchone()

    def test1(self):
        # Do something with self.con or self.cur
        pass

    def test2(self, sql):
	self.cur.execute(sql)
	print('test2 function: '+ sql) 
        pass
    def test3(self):
	self.con.commit()
	print('#3 submit to db: ') 
        pass
    def test4(self, insert, data):
	self.cur.execute(insert,data)
	self.con.commit()
	print('#3 submit to db: ') 
        pass
    def insertData(self, insert, data):
	self.cur.execute(insert,data)
	print('# insert data: ') 
	self.con.commit()
	print('# submit to db: ') 
        pass
    def updateData(self, update, data):
	self.cur.execute(update,data)
	self.con.commit()
	print('#3 submit to db: ') 
        pass
    def test5(self, sql):
	self.cur.execute(sql)
	print('test5 function: '+ sql) 
        return self.cur.fetchall()

if __name__ == '__main__':  # If it's executed like a script (not imported)
    db = MyDBTest()
    #db.show_version()
    db.test1()
    sql = """INSERT INTO rawtable( indexing,
         artist, title, mood)
         VALUES ('Mac1', 'Mohan', '20', 'M')"""
    #db.test2(sql)
    #db.test3()




    # select SQL 
    sql = "SELECT * FROM rawtable2 where lyric = ''"
    
    result = db.test5(sql)     

    # output
    for record in result:
        print record[1]






'''
    #update sql
    update = ("""UPDATE rawtable2 SET mood=%s WHERE indexing=%s""")
    data = ('relaxed','ML1')
    db.test4(update,data)
'''
'''
    #insert sql
    insert = ("INSERT INTO rawtable(indexing, artist, title, mood) VALUES (%s, %s, %s, %s)")
    data = ('Jason','ja','13', '13')
    db.test4(insert,data)
'''





