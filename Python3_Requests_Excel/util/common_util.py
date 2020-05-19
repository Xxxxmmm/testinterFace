#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 野猪佩奇
# @contact : 2790279232@qq.com
# @File    : common_util.py
# @Software: PyCharm
# @Time    : 2020/5/9 16:32
class CommonUtil:
  def is_contain(self, str_one, str_two):
    """
    判断一个字符串是否在另一个字符串中
    :param str_one:
    :param str_two:
    :return:
    """
    flag = None
    if str_one in str_two:
      flag = True
    else:
      flag = False
    return flag