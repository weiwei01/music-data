
import pydbfunction

print(123)

sql = """INSERT INTO rawtable( indexing,
         artist, title, mood)
         VALUES ('Mac1', 'Mohan', '20', 'M')"""

db = pydbfunction.MyDBTest()
db.test2(sql)
db.test3()
