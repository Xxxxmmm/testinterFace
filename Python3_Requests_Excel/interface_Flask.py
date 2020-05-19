#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 野猪佩奇
# @contact : 2790279232@qq.com
# @File    : interface_Flask.py
# @Software: PyCharm
# @Time    : 2020/5/16 16:20
import pymysql
import os
import json
from flask_cors import *
from flask import Flask,request
app = Flask(__name__)
@app.route('/login',methods = ["POST"])
def get_content():
    connect = pymysql.connect("192.168.0.11",
                              port=3306,
                              user="root",
                              password="vpL5L)0hjON31QxHxycZebpzQkRdLcmI",
                              db="ss_mall_plus",
                              )
    cursor = connect.cursor()
    sql = "select * from ums_member;"
    cursor.execute(sql)
    data= cursor.fetchall()
    para = []
    for i in data:
        text = {"id":i[0],"phone":i[2],"status":i[7]}
        para.append(text)
    return json.dumps(para,ensure_ascii=False,indent = 3 )

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port= 9562,debug=True)