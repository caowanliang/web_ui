#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/5/27 21:04
# @Author: william.cao
# @File  : add_path.py

import os
import site

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
USER_PTH = os.path.join(site.getsitepackages()[-1], 'requirements.pth')


def main():
    try:
        os.remove(USER_PTH)
    except FileNotFoundError:
        pass
    with open(USER_PTH, 'w') as f:
        f.write(BASE_DIR)
        print("生成文件成功！")
        print("文件位置：%s" % USER_PTH)
    with open(USER_PTH) as f:
        print("文件内容：", f.read())


if __name__ == '__main__':
    main()