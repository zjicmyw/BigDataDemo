import pandas as pd
import openpyxl
# -------------------------------------
# 1 使用to_excel创建
# -------------------------------------

df=pd.DataFrame({'id':[1,2,3],'content':['a','b','c']})
# 生成excel时，默认会把索引也一并导入
df.set_index('id',inplace=True)
df.to_excel('../cache/excel1.xlsx')


# -------------------------------------
# 2 使用read_excel读取
# -------------------------------------

df2=pd.read_excel('../cache/excel1.xlsx')
'''
   id content
0   1       a
1   2       b
2   3       c
'''
print(df2.shape)
print(df2.columns.tolist())
print(df2.head(1))
print(df2.tail(1))
'''
(3, 2)
['id', 'content']
   id content
0   1       a
   id content
2   3       c
'''

# -------------------------------------
# 3 使用read_sql_query读取 df3=pd.read_sql_query(语句，链接)
# -------------------------------------
