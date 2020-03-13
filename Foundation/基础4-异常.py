#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 自定义异常必须要继承Exception才能用raise抛出

class ContentException(Exception):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return '内容异常,异常数据为：%s' % (self.content)


try:
    content = input('请输入数据')
    if content != '1':
        raise ContentException(content)
except Exception as e:
    print("异常:", e)
else:
    print("经过else")
finally:
    print('最后')
