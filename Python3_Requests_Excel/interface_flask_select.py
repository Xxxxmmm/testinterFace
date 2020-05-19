#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 野猪佩奇
# @contact : 2790279232@qq.com
# @File    : interface_flask_select.py
# @Software: PyCharm
# @Time    : 2020/5/16 16:36
import flask
import pymysql
import os
import json
from flask_cors import *

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask, request

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def get_select():
    inputdata = flask.request.json.get('inputdata')
    data1 = get_content(inputdata)
    return data1


def get_content(inputdata):
    connect = pymysql.connect("192.168.0.11",
                              port=3306,
                              user="root",
                              password="vpL5L)0hjON31QxHxycZebpzQkRdLcmI",
                              db="ss_mall_plus",
                              )
    cursor = connect.cursor()
    sql = "select phone,id from ums_member where phone = '%s'" % (inputdata)
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)
    result = {"id": data[0], "phone": data[2], "status": data[7]}
    return json.dumps(result, ensure_ascii=False, indent=3)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, debug=True)
