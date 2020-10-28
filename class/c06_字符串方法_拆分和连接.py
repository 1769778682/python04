# my_str = "hello world and itcast and itheima and Python"
#
# # split
# # 作用：按照指定字符来分割字符串
# # 语法：字符串.split(分割字符)
# # 需求
#
# # 通过and来分割字符串
# print(my_str.split('and'))
# # 结果
# # ['hello world ', ' itcast ', ' itheima ', ' Python']
#
# # 通过空格分割字符串
# print(my_str.split(' '))  # 通过特定字符拆分字符串
# # 结果
# # ['hello', 'world', 'and', 'itcast', 'and', 'itheima', 'and', 'Python']
#
# new_str = my_str.split(' ')
# for i in new_str:  # 循环遍历获取每一个数据
#     print(i)
#     print(type(i))

# join
# # 作用：一般用于将列表数据按照子字符串合并为字符串
# # 语法：字符串.join（列表）
# # 需求
# # 定义列表数据
# list_data = ['张飞', '刘备', '关羽', '诸葛亮', '百里守约', '百里玄策']
# print(type(' '.join(list_data)))
# new_data = (' '.join(list_data))
# print(new_data)
# str_data = '少小离家老大回'
# print(' '.join(str_data))
#
#
# # 字符串的拼接
# str1 = '好好学习'
# str2 = '天天向上'
# # 需求：将两个字符串合并成一句
# print(str1 + str2)
# 直接用加号也可以拼接列表
str3 = ['好好学习']
str4 = ['天天向上']
print(str3 + str4)



















