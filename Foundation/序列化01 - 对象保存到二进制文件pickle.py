# pickle模块使用的数据格式是python专用的,能够把Python对象,直接保存到文件
# 而不须要把他们转化为字符串，也不用底层的文件訪问操作把它们写入到一个二进制文件中。
import os
import pickle

if not (os.path.exists('BigDataDemo/cache')):
    os.mkdir('BigDataDemo/cache')
# pickle.dump(obj, file[, protocol])
# 序列化对象，并将结果数据流写入到文件对象中。
# 参数protocol是序列化模式，默认值为0，表示以文本的形式序列化。protocol的值还可以是1或2，表示以二进制的形式序列化。

# pickle.load(file)
# 反序列化对象。将文件中的数据解析为一个Python对象。

# 序列化到文件
obj = [123, "abcdedf", ["ac", 123], {"key": "value", "key1": "value1"}]
print(obj)
# wb 读写到二进制文件
f = open("./BigDataDemo/cache/a.txt", 'wb')
pickle.dump(obj, f)
f.close()
f = open("./BigDataDemo/cache/a.txt", 'rb')
print(pickle.load(f))
f.close()


class Teacher(object):
    age = 18
    __type = '黄种人'

    def show(self):
        print('大家好，我是中国老师')


teacher = Teacher()
f2 = open("./BigDataDemo/cache/a2.txt", 'wb')
pickle.dump(teacher, f2)
f2.close()
f2 = open("./BigDataDemo/cache/a2.txt", 'rb')
print(pickle.load(f2))
f2.close()
