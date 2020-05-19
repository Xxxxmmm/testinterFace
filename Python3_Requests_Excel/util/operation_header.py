#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 野猪佩奇
# @contact : 2790279232@qq.com
# @File    : operation_header.py
# @Software: PyCharm
# @Time    : 2020/5/9 16:32
import json
from Python3_Requests_Excel.util.operation_json import OperationJson
from Python3_Requests_Excel.base.runmethond import RunMethod


class OperationHeader:

    def __init__(self, response):
        self.response = json.loads(response)

    # def get_tokenhead(self):
    #     tokenheader = self.response['data']['tokenHead']
    #     return tokenheader

    def get_response_token(self):
        '''
        获取登录返回的token
        '''
        token = {"data": {"authorization": self.response['data']['tokenHead']+self.response['data']['token']}}
        return token

    def write_token(self):
        op_json = OperationJson()
        op_json.write_data(self.get_response_token())


    def get_memberid(self):
        memberid = self.response['data']['userInfo']['id']
        return memberid


if __name__ == '__main__':
    url = "http://192.168.1.209:8085/api/single/home/login"

    data = {
        "phone": "18911113333",
        "password": "111111"
    }
    run_method = RunMethod()
    # res = json.dumps(requests.post(url, data).json())
    res = run_method.run_main('Post', url, data)
    op = OperationHeader(res)
    op.write_token()
    print(op.get_response_token())