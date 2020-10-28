# 1. 在控制台输入 3 组个人信息，
# 每个人有姓名, 年龄, 性别,
# 将信息存入字典中，再将字典存入列表中
# 2. 录入完成后, 遍历列表, 打印每个人的信息
# 定义一个字典
slogan = {}
# 定义一个列表
list1 = []
num = 0
while num < 3:
    print(slogan)
    slogan['姓名'] = input('姓名:')
    slogan['年龄'] = input('年龄:')
    slogan['性别'] = input('性别:')
    num += 1
    # print(slogan.items())
    # 将表连接
    list1.append(slogan.items())
print(list1)

# 遍历表
for k, v in list1:
    print('%s %s' % (k, v))
#
# slogan = {}
# # 定义一个列表
# list1 = []
# num = 0
# while num < 3:
#     list1.append({"name": input('姓名:'),
#                   "age": input('年龄:'),
#                   "sex": input('性别:')})
#     num += 1
#     # print(slogan.items())
#     # 将表连接
#
# print(list1)
#
# # 遍历表
# for i in list1:
#     print(i)
