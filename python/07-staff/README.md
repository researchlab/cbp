
## 00 init && setup project 

```
python3 -m venv /Users/lihong/workbench/dev/src/github.com/researchlab/cbp/python/07-staff

source ./bin/activate
```

## flask setup

```
pip3 install flask
```

## 生成 requirements 

```
pip3 install pipreqs

# 在当前目录生成

pipreqs . --encoding=utf8 --force

--force 强制执行，当 生成目录下的requirements.txt存在时覆盖。

# 使用requirements
pip3 install -r requirements.txt
```

## 00 项目目录 

|---- manage.py # 入口文件
|---- run.sh # 运行脚本
|---- docs # 说明文档
|---- app # 项目包
|------- __init__.py # 初始化模块
|------- configs.py # 配置模块
|------- forms.py # 表单验证模块
|------- models.py # 数据表模型模块
|------- orm.py # 操作数据库会话模块
|------- params.py # 公共参数模块
|------- crud # 增删改查视图包
|---------- __init__.py # 初始化模块
|---------- views_common.py # 公共视图模块
|---------- views_create.py # 增加员工视图模块
|---------- views_read_list.py # 员工列表视图模块
|---------- views_read_one.py # 员工详情视图模块
|---------- views_update.py # 修改员工视图模块
|---------- views_delete.py # 删除员工视图模块
|------- templates # 存放html 的模块目录
|---------- layout.html # 公共布局
|---------- create.html # 添加员工页面
|---------- read_list.html # 员工列表
|---------- read_one.html # 员工详情
|---------- update.html # 修改员工
|------- static # 存放静态资源目录 [css/js/images]


根据以上目录结构 创建对应的目录和空文件


## 01 数据模型设计

员工数据模型

id 编号 大整型 主键 
name 姓名 字符串  非空
job  职位 小整型 非空
sex 性别 小整型  非空
edu 学历  小整型  非空
birth 生日 日期  非空
email 邮箱 字符串 非空 唯一
phone 手机 字符串 非空 唯一
info 介绍 文本 非空
face 头像 字符串  非空
createdAt 添加时间 日期时间  非空
updatedAt 修改时间 日期时间  非空


爱好数据模型【关联员工和爱好】

id 编号 大整型 主键
empolyee_id 员工编号 大整型  非空
hobby_key 爱好索引 小整型 非空
createdAt 添加时间 日期时间  非空
updatedAt 修改时间 日期时间  非空


