# 定义列表
list1 = ['张飞', '刘备', '关羽']
print(list1)

# del
# 作用：删除目标数值
# 语法：del 具体值
del list1[2]  # 删除单个数据
print(list1)
del list1  # 移除列表对象，再次调用提示列表不存在
# NameError: name 'list1' is not defined

# pop
# 作用：可以删除指定下标的数据
# 语法：列表.pop（索引）
list1.pop(0)
print(list1)
# 注意：使用pop时，如果()里面没有值，默认删除最后一个值
list1.pop()
print(list1)

# remove
# 作用：在列表中删除一个具体数据，删除第一个符号要求的
# 语法：列表.remove（目标值）
print(list1)
list1.remove('刘备')
print(list1)

# clear
# 作用：请空列表
# 语法：列表.clear()
list1.clear()
print(list1)





