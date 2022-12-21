import peewee 
db = peewee.SqliteDatabase('sql.db')

class Teacher(peewee.Model):
    name = peewee.CharField(max_length=20, default='mike')
    age = peewee.IntegerField()

    class Meta:
        database = db

if __name__ == '__main__':
    # 创建表
    Teacher.create_table()
    # 增加
    T = Teacher()
    T.name = 'jack'
    T.age = 18
    T.save()

    # 增加 
    T = Teacher().insert(
            name='tony',
            age= 18,
            )
    T.execute()

    # 删除
    T = Teacher.delete().where(Teacher.id == 1)
    T.execute() 
    # 修改
    T = Teacher.update(name='tony').where(Teacher.id == 1)
    T.execute()

    T = Teacher().get(id = 2)
    T = Teacher.get_by_id(2)
    T.name = 'jack'
    T.save()

    # 查找
    T_list = Teacher.select()
    for i in T_list:
        print(i.name, i.age)
    T_list = Teacher.select().order_by(Teacher.age)
    for i in T_list:
        print(i.name, i.age)
    # 查一条
    T_list = Teacher.select().where(Teacher.age == 18)
    for i in T_list:
        print(i.name, i.age)
    T = Teacher.get(id=2)
    print(T.name, T.age)
