# 复制
# 语法：列表.copy()
list1 = [1, 2, 3, 4]
list2 = list1.copy()  # 复制：将原数据制作一个新的副本，新数据
list3 = list1  # list1和list3指向的是同一份数据
list1.append(5)
print(list1)
print(list2)
print(list3)

# for循环
# 可以通过for循环遍历列表数据
list4 = ['张飞', '刘备', '关羽']
for i in list4:
    print(i)


# 列表嵌套
# 注意：
# 1，列表可以多层嵌套
# 2.无论是几层嵌套，都可以通过索引（下标）进行访问
per = [['张飞1', '刘备1', '关羽1'], ['张飞2', '刘备2', '关羽2']]
print(per[0][0])










