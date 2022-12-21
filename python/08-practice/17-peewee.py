import peewee 
import datetime 

# connect database 
connect = peewee.MySQLDatabase(
        database = 'mytest',
        host = 'localhost',
        user = 'root',
        passwd = 'root'
        )

class School(peewee.Model):
    name = peewee.CharField(max_length=20, default='mike')
    address = peewee.CharField(max_length=30, default='china')
    age = peewee.CharField(default=18)
    birthday = peewee.DateTimeField(default=datetime.datetime.now())

    # 将表和数据库链接起来
    class Meta:
        database = connect

if __name__ == "__main__":
    # 创建表
    School.create_table()

    # 插入数据
    s = School.create(name='mike', age=12, birthday='2022-10-10')
    s.save()

    # 第二种插入方法
    School.insert(name='jack', age=18, birthday='2018-06-12').execute()

    # 更新
    School.update(name='tony',age=10,
            birthday='2018-10-11').where(School.id==1).execute()

    # 删除数据
    # s = School.get(name='tony')
    # s.delete_instance()

    # 第二种删除 
    # School.delete_by_id(2)
    # School.delete().where(School.id == 5).execute()

    # 查询语句
    s = School.select()
    for i in s:
        print(i.name, i.age)

    ss = School.get(School.id == 1)
    print(ss.name, ss.age)

    # 有条件查询
    sss = School.select().where(School.id == 2)
    for i in s:
        print(i.name)

    # 正序查询， 倒序查询
    s = School.select().order_by(School.id.asc())
    s = School.select().order_by(School.id.desc())
    for i in s:
        print(i.age)
