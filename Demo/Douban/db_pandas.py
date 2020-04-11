import pandas as pd
import sys
import matplotlib.pyplot as plt
import matplotlib
from pyecharts.charts import Bar
from pyecharts import options as opts
# 豆瓣top250电影分析：

# 1、加载数据
data=pd.read_csv('asset/dbtop250.csv',encoding='gbk')

# 2、查看基本信息
# print(data.info())
'''
<class 'pandas.core.frame.  '>
Int64Index: 244 entries, 0 to 249
Data columns (total 10 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   排名      250 non-null    int64
 1   片名      250 non-null    object
 2   分数      250 non-null    float64
 3   评价人数    250 non-null    int64
 4   简评      249 non-null    object
 5   导演      250 non-null    object
 6   主演      245 non-null    object
 7   年份      250 non-null    object
 8   国家/地区   250 non-null    object
 9   类型      250 non-null    object
dtypes: float64(1), int64(2), object(7)
memory usage: 19.7+ KB
'''
# 共有250行 10个字段，简评      249，主演      245缺失值

# 3、处理缺失值
data.iloc[:, 4].fillna('无', inplace=True) # 填充指定列
data.iloc[:, 6].fillna('未知', inplace=True) # 填充指定列

#检查是否有重名电影
# print(data.duplicated().value_counts())
'''
False    250
dtype: int64
'''
# -------------------------------------
# 
# 1 分析'国家/地区'
# 
# [List].apply(pd.Series)# 将一列 转化为 DataFrame
# [DataFrame].apply(pd.value_counts) 统计并返回新的 DataFrame
# -------------------------------------

'''
Series对象的apply方法是指对其中的每个元素进行映射。
pd.Series方法将[data[列名].str.split(' ')]的中list元素转为Series。
Series对象的apply方法和pd.Series方法结合自动实现Series对象转换为DataFrame对象。
'''

df_country =data['国家/地区'].str.split(' ').apply(pd.Series)# 将一列变为新的 DataFrame
# print(df_country)
'''
        0     1    2    3    4    5
0      美国   NaN  NaN  NaN  NaN  NaN
1    中国大陆  中国香港  NaN  NaN  NaN  NaN
2      美国   NaN  NaN  NaN  NaN  NaN
3      法国   NaN  NaN  NaN  NaN  NaN
4     意大利   NaN  NaN  NaN  NaN  NaN
..    ...   ...  ...  ...  ...  ...
245    美国   俄罗斯  NaN  NaN  NaN  NaN
246    美国   NaN  NaN  NaN  NaN  NaN
247    美国    德国  NaN  NaN  NaN  NaN
248    美国   NaN  NaN  NaN  NaN  NaN
249    美国   NaN  NaN  NaN  NaN  NaN
'''

# 将空值 NaN 替换为“0”，再转为int,按行汇总。
df_all_country = df_country.apply(pd.value_counts).fillna('0')
'''
  0   1  2  3  4  5
中国台湾    6   2  0  0  0  0
中国大陆   16   5  1  0  0  0
'''
df_all_country.columns = ['area1','area2','area3','area4','area5','area6']# 重命名
df_all_country['area1'] = df_all_country['area1'].astype(int)# astype(int)将dateframe某列的str类型转为int
df_all_country['area2'] = df_all_country['area2'].astype(int)
df_all_country['area3'] = df_all_country['area3'].astype(int)
df_all_country['area4'] = df_all_country['area4'].astype(int)
df_all_country['area5'] = df_all_country['area5'].astype(int)
df_all_country['area6'] = df_all_country['area6'].astype(int)
df_all_country['all_counts'] = df_all_country['area1']+df_all_country['area2']+df_all_country['area3']+df_all_country['area4']+df_all_country['area5']+df_all_country['area6']
df_all_country.sort_values(['all_counts'],ascending=False, inplace=True)# 降序
# print(df_all_country.head())
'''
      area1  area2  area3  area4  area5  area6  all_counts
美国      118     13      3      4      0      0         138
日本       32      2      0      0      0      0          34
英国       14     15      4      0      0      0          33
中国香港     18      8      0      1      0      0          27
中国大陆     16      5      1      0      0      0          22
'''
# -------------------------------------
# 2 分析'类型'
# 
# [DataFrame].apply(lambda x:x.value_counts())
# DataFrame].apply(lambda x:x.sum(), axis=1)
# -------------------------------------

df_type = data['类型'].str.split(' ').apply(pd.Series)
# print(df_type.head(2))
'''
    0   1    2    3    4
0  犯罪  剧情  NaN  NaN  NaN
1  剧情  爱情   同性  NaN  NaN
'''

df_type_count_colmuns = df_type.apply(lambda x:x.value_counts()) #统计value相同的数值
# print(df_type_count_colmuns.head())
'''
        0     1     2    3    4
传记    2.0  10.0   1.0  NaN  NaN
儿童    1.0   3.0   1.0  NaN  NaN
冒险    3.0   8.0  22.0  9.0  2.0
剧情  164.0  16.0   4.0  NaN  NaN
动作   17.0  13.0   3.0  NaN  NaN
'''
ser_type_count = df_type_count_colmuns.apply(lambda x:x.sum(), axis=1).sort_values(ascending=False)
# print(ser_type_count.head())
'''
剧情    184.0
爱情     55.0
喜剧     51.0
犯罪     46.0
冒险     44.0
dtype: float64
'''

bar = (
        Bar()
        .add_xaxis(list(ser_type_count.index))
        .add_yaxis("豆瓣TOP250电影", list(ser_type_count))
        .set_global_opts(
                xaxis_opts=opts.AxisOpts(name_gap=20)
        )
        .render('../cache/电影类型分析柱状图.html')
)

# -------------------------------------
# 3 分析'导演'
# 
# [Series].value_counts()
# -------------------------------------


ser_director = data['导演'].value_counts()
#series 转dataframe 
'''
克里斯托弗·诺兰 Christopher Nolan                 7
 宫崎骏 Hayao Miyazaki                         7
'''
df_director = pd.DataFrame({'name':ser_director.index,'counts':ser_director.values})
# print(df_director.head())
'''
                          name  counts
0   克里斯托弗·诺兰 Christopher Nolan       7
1           宫崎骏 Hayao Miyazaki       7
2   史蒂文·斯皮尔伯格 Steven Spielberg       7
3                   李安 Ang Lee       5
4             王家卫 Kar Wai Wong       5
'''

# -------------------------------------
# 4 分析排名和分数的关系
# -------------------------------------

'''#配置中文字体和修改字体大小
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.size'] = 20

plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
plt.scatter(data['分数'],data['排名'])
plt.xlabel('评分')
plt.ylabel('排名')
#修改y轴为倒序
plt.gca().invert_yaxis()

#集中趋势的直方图
plt.subplot(1,2,2)
plt.hist(data['分数'],bins=15)

# print('电影排名和分数的相关性:',data['分数'].corr(data['排名']))
# 电影排名和分数的相关性: -0.7344352078758816
# plt.show()'''

# -------------------------------------
# 5 分析电影产量年份
# -------------------------------------

group_by_year_dir=data.groupby('年份')['导演'].count()
# print(group_by_year_dir)  
plt.figure() # 设置画布
group_by_year_dir.plot() # 画图
# plt.show()

print('分析完成')

