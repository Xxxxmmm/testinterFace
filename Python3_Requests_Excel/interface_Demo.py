#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 野猪佩奇
# @contact : 2790279232@qq.com
# @File    : interface_Demo.py
# @Software: PyCharm
# @Time    : 2020/5/16 15:52
import pymysql
import os
def get_user():
    connect = pymysql.connect("192.168.0.11",
        port = 3306,
        user = "root",
        password = "vpL5L)0hjON31QxHxycZebpzQkRdLcmI",
        db = "ss_mall_plus",
    )
    cursor = connect.cursor()
    sql = "select * from ums_member"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    para = []
    for i in data:
        text = {"id":i[0],"phone":i[2],"status":i[7]}
        print(text)
        para.append(text)
get_user()