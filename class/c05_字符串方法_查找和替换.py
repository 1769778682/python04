# 定义一个字符串
# str_data = '少小离家老大回，乡音无改鬓毛衰'

# 查找和替换功能
# find
# 字符串.find（目标字符串，开始位置，结束位置）
# print(str_data.find('回'))  # 如果目标存在，则返回目标的索引值
# print(str_data.find('哈'))  # 如果目标不存在，则返回-1
# print(str_data.find('回', 0, 2))  # 可以通过起始索引和借宿索引限定查找范围

# index
# 字符串.index（目标字符串，开始位置，结束位置）

# count
# 统计目标字符出现次数
# 语法：字符串.count(目标，开始位置，结束位置）
# print(str_data.count('回'))
# print(str_data.count('哈'))
# print(str_data.count('回', 5, 7))

# replace
# 使用新字符串，按照规则替换旧字符串
# 语法：字符串.replace（旧字符串，新字符串，替换次数）
str_data = '传智播客在线教育，传智播客线下教育'
new_data = str_data.replace('传智播客', '黑马', 1)
new_data1 = str_data.replace('传智播客', '黑马')
print(str_data)
print(new_data)
print(new_data1)




