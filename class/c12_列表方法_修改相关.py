# 定义列表
list1 = ['张飞', '刘备', '关羽']
print(list1)

# 通过下标（索引）修改（重点）
# 作用：制定目标的下标修改数据
# 语法：列表[下标] = 修改后的值

list1[1] = '赵云'
print(list1)

# reverse
# 作用：倒置列表中的元素
# 语法: list1.reverse()
list1.reverse()
print(list1)


# 排序
# 作用:让列表按照指定规则(升序/降序)排序
# 语法：列表.sort(reverse=False)
list2 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
list2.sort()  # 默认为升序，等价于reverse=False 升序
print(list2)
list2.sort(reverse=False)  # reverse=False 升序
print(list2)
list2.sort(reverse=True)  # reverse=True 降序
print(list2)










