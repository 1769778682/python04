# 定义一个列表
list1 = ['张飞', '刘备', '关羽', '关羽']

# 通过索引获取数据  （重点）
# print(list1[1])  # 正向索引
# print(list1[-1])  # 逆向索引

# index
# 查找目标数据，返回对应下标
# 语法：列表.index(数据)
# print(list1.index('关羽'))

# count
# 作用：统计目标值出现的次数
# 语法：列表.count(目标值)
# print(list1.count('关羽'))

# len （重点）
# 作用：统计列表中元素的个数（列表的长度）
# 语法：len(列表)
# print(len(list1))

# 遍历列表
for i in list1:
    print(i)


for i in range(len(list1)):  # 配合for循环一起使用
    print(i)

# for i in range(4):  # 配合for循环一起使用
#     print(i)













