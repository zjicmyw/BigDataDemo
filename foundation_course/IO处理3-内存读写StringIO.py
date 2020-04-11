# 存入内存和存变量区别：内存地址不改变
import io

# 文字

str_io = io.StringIO()

str_io.write('hello')
str_io.write('world')

print(str_io.getvalue())

print(str_io.read())
# 设置文件指针
str_io.seek(0)
print(str_io.read())

# 二进制：视音频图片

byte_io = io.BytesIO()
byte_io.write('你好'.encode('utf-8'))
print(byte_io.getvalue().decode('utf-8'))
