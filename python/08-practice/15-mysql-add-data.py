import pymysql 

db = pymysql.connect(host='localhost', user='root', password='root',
        database='mytest', charset='utf8')

cursor = db.cursor()

cursor.execute("insert into test_sql(name,age) value('mike',19)")

# 提交到数据库
db.commit()

cursor.close() 
db.close()
