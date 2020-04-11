
# 递归
def calc_num(num):
    if num == 1:
        return 1
    else:
        print(num)
        return num * calc_num(num - 1)


result = calc_num(5)
print('result:', result)
