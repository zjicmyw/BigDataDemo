import pandas as pd
from pandas import Series, DataFrame
import numpy as np


def newprint(content):
    print('-' * 30)
    print(content, ':')


# 索引
newprint('索引')
df1 = pd.DataFrame(np.arange(9).reshape(3, 3), index=['bj', 'sh', 'sz'])
print(df1)
print(list(df1.index))
df1.index = ['bj2', 'sh2', 'sz2']
print(df1)
'''
   0  1  2
bj  0  1  2
sh  3  4  5
sz  6  7  8
['bj', 'sh', 'sz']
     0  1  2
bj2  0  1  2
sh2  3  4  5
sz2  6  7  8
'''


def test_map(x):
    return str(x)+'_AAA'


# rename 返回新的DataFrame
df2 = df1.rename(index=test_map, columns=test_map)
print(df2)
'''
         0_AAA  1_AAA  2_AAA
bj2_AAA      0      1      2
sh2_AAA      3      4      5
sz2_AAA      6      7      8
'''
# 修改指定行列只能rename
df3 = df1.rename(index={'bj2': 'bj3', 'sz2': 'sz3'}, columns={0: 4})
print(df3)
'''
     4  1  2
bj3  0  1  2
sh2  3  4  5
sz3  6  7  8
'''
# 把DF的一列设置成索引
print('把DF的一列设置成索引')
print(df3.set_index(4))
print(df3.set_index(4, drop=False))
'''
   1  2
4
0  1  2
3  4  5
6  7  8
   4  1  2
4
0  0  1  2
3  3  4  5
6  6  7  8
'''

newprint('添加数据：列')
# 增加一列 方法1
df2['3_Aaa'] = [2, 3, 4]
print(df2)
'''
         0_AAA  1_AAA  2_AAA  3_Aaa
bj2_AAA      0      1      2      2
sh2_AAA      3      4      5      3
sz2_AAA      6      7      8      4
'''
# 增加一列 方法2：指定位置
col_name = df2.columns.tolist()
col_name.insert(4, '4_aaa')
'''
rename
更改行名列名。传入的函数或字典值必须是1对1的，没有包含在字典或者Series中的标签将保持原来的名称。
reindex
重建索引，对于索引没有对应值的，使用 NaN 或者指定的值填充。
'''
df3 = df2.reindex(columns=col_name)
print(df3)
df3['4_aaa'] = [3, 4, 6]
print(df3)
'''
         0_AAA  1_AAA  2_AAA  3_Aaa  4_aaa
bj2_AAA      0      1      2      2    NaN
sh2_AAA      3      4      5      3    NaN
sz2_AAA      6      7      8      4    NaN
         0_AAA  1_AAA  2_AAA  3_Aaa  4_aaa
bj2_AAA      0      1      2      2      3
sh2_AAA      3      4      5      3      4
sz2_AAA      6      7      8      4      6
'''
# 增加一列 方法3：指定位置
df2.insert(4, '4_aaa', [2, 5, 8])
print(df2)
'''
         0_AAA  1_AAA  2_AAA  3_Aaa  4_aaa
bj2_AAA      0      1      2      2      2
sh2_AAA      3      4      5      3      5
sz2_AAA      6      7      8      4      8
'''

newprint('增加数据：行')
df4 = pd.DataFrame({'0_AAA': 1, '1_AAA': 2, '2_AAA': 3,
                    '3_Aaa': 4, '4_aaa': 5}, index=[1])
df5 = df2.append(df4)
# 数字时候使用，可以根据自动递增，设置index
df6 = df2.append(df4, ignore_index=True)
print(df5)
print(df6)


# 多重索引:方法1
newprint('多重索引')
df7 = DataFrame(np.random.randint(0, 100, (6, 4)), index=[list('aabbcc'), [
                '期中', '期末', '期中', '期末', '期中', '期末']], columns=['甲', '以', '并', '定'])
# 多重索引:方法2
i1 = ['语文', '数学', '英语']
i2 = ['期中', '期末']
index1 = pd.MultiIndex.from_product([i1, i2])
df8 = DataFrame(np.random.randint(0, 100, size=(6, 4)),
                index=index1, columns=['甲', '以', '并', '定'])
print(df8)
'''
        甲   以   并   定
语文 期中  36  28  56  57
   期末  31  66   2  69
数学 期中  36  87  86  46
   期末  95  20  21  48
英语 期中  44  56  44  78
   期末  24  66  93  35
'''
# 多重索引取值
print(df8['甲'])  # 得到甲的所有成绩
print(df8.loc['语文'])  # 得到语文的所有成绩
print(df8.loc['语文', '期末'])  # 得到语文期末的所有成绩
print(df8.loc['语文', '期末']['甲'])  # 得到甲的语文期末的所有成绩
'''
语文  期中    36
    期末    31
数学  期中    36
    期末    95
英语  期中    44
    期末    24

Name: 甲, dtype: int32

     甲   以   并   定
期中  36  28  56  57
期末  31  66   2  69
甲    31
以    66
并     2
定    69
Name: (语文, 期末), dtype: int32
31
'''
