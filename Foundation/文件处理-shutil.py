import os
import shutil


# 切换到指定路径
os.chdir('BigDataDemo')
print(os.getcwd())

# 删除文件/文件夹 (文件夹中有文件时候，可以删除)
shutil.rmtree('cache')