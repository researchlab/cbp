# python flask 实践 加载 echarts  配合 bootstrap 5 

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

### flask 加载图片和css 等动态文件的方法

用 url_for() 方法
`<link rel="stylesheet" href="{{url_for('static', filename='css/style.css')}}">`

上面第一个是static, 按资料是应该要建立一个static目录， 然后在static目录中存放静态资源，但是实际访问的时候，发现请求是来自 templates目录，所以这里根据实际情况把css文件夹建立在templates目录下了， 上面还是用static

### echarts 图片自适应页面大小而改变

```
var chart = echarts.init(document.getElementById("map"), "white",{renderer:"canvas"});
window.addEventListener("resize",function(){
									chart.resize();
				})
```

### flex 布局，单个元素要靠右

父元素使用 display:flex 
要靠右边的子元素使用 margin-left:auto;

### flask 跨域问题

本文仅做实践，所以使用的是localhost, 如果使用127.0.0.1 需要解决跨域问题

### 解决菜单点击高亮问题

```
            $('#sidebar ul li').click(function(){
                $('#sidebar ul li').removeClass('active')
                $(this).addClass('active')
            })

```

### 解决菜单栏点击隐藏

用的toggleClass

```
            $(document).ready(function(){
                $('#sidebarCollapse').on('click',function(){
                    $('#sidebar').toggleClass('active')
                })
            })
```
