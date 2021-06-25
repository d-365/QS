# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 14:06
# @Author  : dujun
# @File    : other2.py
# @describe:

# import sys
# print(len(sys.argv))
# print(sys.argv[0])
# print(sys.argv[0])

import argparse

parser = argparse.ArgumentParser('切换测试环境')
parser.add_argument('-test', '--test', default=1, type=int, help='just for help')
args = parser.parse_args()

print(args.test)
