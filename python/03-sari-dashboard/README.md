
### init project 

```shell
# init project
python3 -m venv /Users/lihong/workbench/dev/src/github.com/researchlab/cbp/python/03-sari-dashboard

# activate project 
source ./bin/activate

# deactivate
deactivate
```

### tips 

```shell
# pip 一次安装多个包, 如一次安装requests-html flask pyecharts
pip3 install requests-html flask pyecharts
```

### requirements 

生成requirements 两个方法

```shell
# 方法一 (只能用在单独环境)
pip freeze > requirements.txt

# 方法二 推荐 (可用在全局环境)
# 安装

pip install pipreqs

# 在当前目录生成

pipreqs . --encoding=utf8 --force

--force 强制执行，当 生成目录下的requirements.txt存在时覆盖。

# 使用requirements 
pip install -r requirements.txt
```




