# 现有两个列表: [1,3,5,7,9] 和 [2,4,6,8,0], 如何将他们合并后并排序?
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 0]
print(list1)
print(list2)
# 将 表2 接到 表1 后边
list1.extend(list2)
print(list1)
# 排序
list1.sort(reverse=False)
print(list1)
