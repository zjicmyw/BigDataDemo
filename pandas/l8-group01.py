import pandas as pd
import numpy as np
import random

df = pd.DataFrame({
    'name': ['BOSS', 'Lilei', 'Lilei', 'Han', 'BOSS', 'BOSS', 'Han', 'BOSS'],
    'Year': [2016, 2016, 2016, 2016, 2017, 2017, 2017, 2017],
    'Salary': [999999, 20000, 25000, 3000, 9999999, 999999, 3500, 999999],
    'Bonus': [100000, 20000, 20000, 5000, 200000, 300000, 3000, 400000]
})
'''
    name  Year   Salary   Bonus
0   BOSS  2016   999999  100000
1  Lilei  2016    20000   20000
2  Lilei  2016    25000   20000
3    Han  2016     3000    5000
4   BOSS  2017  9999999  200000
5   BOSS  2017   999999  300000
6    Han  2017     3500    3000
7   BOSS  2017   999999  400000
'''
# 根据name这一列进行分组
group_by_name = df.groupby('name')
'''
{'BOSS': Int64Index([0, 4, 5, 7], dtype='int64'),
 'Han': Int64Index([3, 6], dtype='int64'), 
'Lilei': Int64Index([1, 2], dtype='int64')}

       Year  Salary  Bonus
name
BOSS      4       4      4
Han       2       2      2
Lilei     2       2      2
'''
# 查看分组的情况
# for name,group in group_by_name:
#     print(name) # 组的名字
#     print(group) # 组具体内容
'''
BOSS
   name  Year   Salary   Bonus
0  BOSS  2016   999999  100000
4  BOSS  2017  9999999  200000
5  BOSS  2017   999999  300000
7  BOSS  2017   999999  400000
Han
  name  Year  Salary  Bonus
3  Han  2016    3000   5000
6  Han  2017    3500   3000
Lilei
    name  Year  Salary  Bonus
1  Lilei  2016   20000  20000
2  Lilei  2016   25000  20000
'''
# 按照某一列进行分组, 将name这一列作为分组的键，对year进行分组
group_by_name = df['Year'].groupby(df['name'])
'''
BOSS
0    2016
4    2017
5    2017
7    2017
Name: Year, dtype: int64
Han
3    2016
6    2017
Name: Year, dtype: int64
Lilei
1    2016
2    2016
Name: Year, dtype: int64
'''

# 按照多列进行分组
group_by_name_year = df.groupby(['name', 'Year'])
'''
('BOSS', 2016)
   name  Year  Salary   Bonus
0  BOSS  2016  999999  100000
('BOSS', 2017)
   name  Year   Salary   Bonus
5  BOSS  2017   999999  300000
7  BOSS  2017   999999  400000
('Han', 2016)
  name  Year  Salary  Bonus
3  Han  2016    3000   5000
('Han', 2017)
  name  Year  Salary  Bonus
6  Han  2017    3500   3000
('Lilei', 2016)
    name  Year  Salary  Bonus
1  Lilei  2016   20000  20000
2  Lilei  2016   25000  20000
'''

# 可以选择分组
print(group_by_name.get_group('BOSS'))
# 可以选择分组
print(group_by_name_year.get_group(('BOSS', 2016)))
'''
0    2016
4    2017
5    2017
7    2017
Name: Year, dtype: int64
--------------------
   name  Year  Salary   Bonus
0  BOSS  2016  999999  100000
'''
