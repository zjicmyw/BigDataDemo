import os

# 查看当前路径
print(os.getcwd())

# # 创建文件夹,路径默认为当前
# os.mkdir('BigDataDemo/cache')

# # 创建文件,路径默认为当前
# file = open('BigDataDemo/cache/a.txt', 'w', encoding='utf-8')

# # 切换到指定路径
# os.chdir('BigDataDemo/cache')
# print(os.getcwd())

# # 改名 文件/文件夹
# os.rename('a.txt', 'b.txt')

# 删除文件/文件夹 (文件夹中有文件时候，不可以删除)
# os.remove('b.txt')