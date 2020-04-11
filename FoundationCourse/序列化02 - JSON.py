import os
import json

if not (os.path.exists('BigDataDemo/cache')):
    os.mkdir('BigDataDemo/cache')

# 序列化到文件
obj = [123, "你好", ["ac", 123], {"key": "value", "key1": "value1"}]
print(obj)
f = open("./BigDataDemo/cache/c.txt", 'w', encoding='utf-8')
json.dump(obj, f)
f.close()
f = open("./BigDataDemo/cache/c.txt", 'r', encoding='utf-8')
print(json.load(f))
f.close()


class Teacher(object):
    age = 18
    __type = '黄种人'

    def __init__(self):
        self.name = '张三'

    def show(self):
        print('大家好，我是中国老师')


teacher = Teacher()
f2 = open("./BigDataDemo/cache/c2.txt", 'w', encoding='utf-8')
# 序列化 类的实例属性，类属性不涉及
print(teacher.__dict__)
json.dump(teacher.__dict__, f2)
f2.close()
f2 = open("./BigDataDemo/cache/c2.txt", 'r', encoding='utf-8')
print(json.load(f2))
f2.close()
