import pymysql 

db = pymysql.connect(host='localhost', user='root', password='root',
        database='mytest', charset='utf8')

cursor = db.cursor()

cursor.execute("drop table test_sql")

db.commit()

cursor.close()
db.close()
