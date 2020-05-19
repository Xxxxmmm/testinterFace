#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 野猪佩奇
# @contact : 2790279232@qq.com
# @File    : run_test.py
# @Software: PyCharm
# @Time    : 2020/5/9 16:31
from Python3_Requests_Excel.base.runmethond import RunMethod
from Python3_Requests_Excel.data.get_data import GetData
from Python3_Requests_Excel.util.common_util import CommonUtil
from Python3_Requests_Excel.data.dependent_data import DependentData
# from util.send_email import SendEmail
from Python3_Requests_Excel.util.operation_header import OperationHeader
from Python3_Requests_Excel.util.operation_json import OperationJson


class RunTest:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        # self.send_email = SendEmail()

    def go_on_run(self):
        """程序执行"""
        pass_count = []
        fail_count = []
        res = None
        # 获取用例数
        rows_count = self.data.get_case_lines()
        # 第一行索引为0
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                expect = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)

                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    # 更新请求字段
                    request_data[depend_key] = depend_response_data
                # 如果header字段值为write则将该接口的返回的token写入到token.json文件，如果为yes则读取token.json文件
                if header == "write":
                    res = self.run_method.run_main(method, url, request_data)
                    op_header = OperationHeader(res)
                    op_header.write_token()
                elif header == 'yes':
                    op_json = OperationJson("../dataconfig/token.json")
                    header = op_json.get_data('data')
                    token = op_json.get_data('data')
                    request_data = dict(request_data,**token)
                    res = self.run_method.run_main(method,url,request_data,header=header)
                else:
                    res = self.run_method.run_main(method, url, request_data)

                if expect != None:
                    if self.com_util.is_contain(expect, res):
                        self.data.write_result(i, "【Pass】")
                        print("=====第【%s】行用例执行成功】=====" % i)
                        pass_count.append(i)
                    else:
                        self.data.write_result(i,res)
                        print("=====第【%s】行用例执行失败】=====错误响应信息如下=====\n" % i)
                        print(f'\033[1;31m{res}\033[0m')    #前景色，背景色
                        fail_count.append(i)
                else:
                    print(f"用例ID：case-{i}，预期结果不能为空\n")

        # 发送邮件
        # self.send_email.send_main(pass_count, fail_count)
        print(f"=====通过用例数=====：【{len(pass_count)}】")
        print(f"=====失败用例数=====：【{len(fail_count)}】")


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()