import pymysql 

db = pymysql.connect(host='localhost', user='root',password='root', database='mytest', charset='utf8')

cursor = db.cursor()

sql = '''create table test_sql(
id INT PRIMARY KEY auto_increment,
name VARCHAR(30),
age INT
)'''

cursor.execute(sql)

cursor.close()

db.close()
