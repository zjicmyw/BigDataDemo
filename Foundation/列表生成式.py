
# 列表生成式 类似map
my_list = []
my_list = [val for val in range(0, 6)]
print(my_list)
# 场景：便捷的统计每一项长度
my_list1 = [len(val) for val in ['a', 'bb', 'accc']]
print(my_list1)
# 场景：统一操作
my_list2 = [val * 2 + 1 for val in range(0, 6)]
print(my_list2)
# 场景：if结合
my_list3 = [val for val in range(1, 15) if val % 2 == 0]
print(my_list3)
