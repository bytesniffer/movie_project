#!/usr/bin/ python
# -*- coding: utf-8 -*-
__author__ = 'mtianyan'
__date__ = '2018-11-27 23:59'
"""
            　┏┓　　　┏┓+ +
  　　　　　　　┏┛┻━━━┛┻┓ + +
  　　　　　　　┃　　　　　　　┃ 　
  　　　　　　　┃　　　━　　　┃ ++ + + +
  　　　　　　 ████━████ ┃+
  　　　　　　　┃　　　　　　　┃ +
  　　　　　　　┃　　　┻　　　┃
  　　　　　　　┃　　　　　　　┃ + +
  　　　　　　　┗━┓　　　┏━┛
  　　　　　　　　　┃　　　┃　　　　　　　　　　　
  　　　　　　　　　┃　　　┃ + + + +
  　　　　　　　　　┃　　　┃　　　　Code is far away from bug with the animal protecting　　　　　　　
  　　　　　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
  　　　　　　　　　┃　　　┃
  　　　　　　　　　┃　　　┃　　+　　　　　　　　　
  　　　　　　　　　┃　 　　┗━━━┓ + +
  　　　　　　　　　┃ 　　　　　　　┣┓
  　　　　　　　　　┃ 　　　　　　　┏┛
  　　　　　　　　　┗┓┓┏━┳┓┏┛ + + + +
  　　　　　　　　　　┃┫┫　┃┫┫
  　　　　　　　　　　┗┻┛　┗┻┛+ + + +
"""

SQL_URL = '127.0.0.1'
SQL_USER = 'root'
SQL_PASSWORD = '123456'
DATABASE = 'movie'
ADMIN = 'waert'
ADMIN_PASSWORD = '123456'

SQLALCHEMY_DATABASE_URI = """mysql+pymysql://{SQL_USER}:{SQL_PASSWORD}@{SQL_URL}:3306/{DATABASE}""".format(
                          SQL_USER=SQL_USER,
                          SQL_PASSWORD=SQL_PASSWORD,
                          SQL_URL=SQL_URL,
                          DATABASE=DATABASE)
