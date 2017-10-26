import sys

import pymysql

class MyDBTest():

    def __init__(self):
        try:
            self.con = pymysql.connect("localhost","phpmyadmin","12qwaszx","musicdb" )
            self.cur = self.con.cursor()
	    self.show_version()
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

if __name__ == '__main__':  # If it's executed like a script (not imported)
    db = MyDBTest()
    #db.show_version()
    db.test1()
    sql = """INSERT INTO rawtable( indexing,
         artist, title, mood)
         VALUES ('Mac1', 'Mohan', '20', 'M')"""
    db.test2(sql)
    db.test3()

