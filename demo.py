#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 野猪佩奇
# @contact : 2790279232@qq.com
# @File    : demo.py
# @Software: PyCharm
# @Time    : 2020/5/16 18:18
import pymysql
import json
connect = pymysql.connect(
    host = "192.168.0.11",
    port = 3306,
    user = "root",
    password = "vpL5L)0hjON31QxHxycZebpzQkRdLcmI",
    db = "ss_mall_plus"
)
corsor= connect.cursors()
sql = "select * from ums_member;"
corsor.ex