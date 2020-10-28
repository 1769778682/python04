# 定义列表
# list1 = ['张飞', '刘备', '关羽']
# print(list1)
# append（重点）
# 作用：在列表末尾添加数据
# 语法：列表.append（数据）
# 需求：
#
# # 增加赵云到列表中
# list1.append('赵云')
# print(list1)
#
# # 如果增加的数据是个列表，会将整个列表作为一个值添加至末尾
# list1.append([1, 2, 3])
# print(list1)

# extend
# 作用：将另一个列表接到本列表尾部，接上后，列表合并为本列表
# 语法：列表.extend(列表2)
list2 = [1, 2, 3, 4]
list3 = [5, 6, 7, 8]
list2.extend(list3)
print(list2)

# # insert
# # 作用：在指定位置插入新数据
# # 语法：列表.insert（指定位置索引，数据）
# list1.insert(0, '赵云')
# print(list1)
# # 注意：列表是有序类型数据（通过索引可以获取对应元素）



