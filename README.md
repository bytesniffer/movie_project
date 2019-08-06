# Flask 弹幕微电影

[![Build Status](https://travis-ci.org/mtianyan/hexoBlog-Github.svg?branch=master)](https://travis-ci.org/mtianyan/hexoBlog-Github)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)


## 项目下载及运行:

- 基础运行环境安装:

```
git clone https://github.com/mtianyan/movie_project
cd movie_project
pip install -r requirement.txt
# 新建一个movie数据库(自行新建) ; 修改config目录下的base_config中数据库用户密码，管理员用户密码
python generate_tables.py
python manage.py runserver
```

打开网址: http://127.0.0.1:5000/ 访问首页; http://127.0.0.1:5000/admin 访问后台。



# Python 3

pip3 freeze > requirements.txt 

pip3 install -r requirements.txt 

# Run
python manage.py runserver
# TO-DO list

* 电影列表优化　
* 标签优化


