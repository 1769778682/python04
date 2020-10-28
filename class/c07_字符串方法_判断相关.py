# startswith
# 作用：判断字符串是否以xxx开头
# 语法：字符串.startswith（目标内容，开始位置，结束位置）
# 需求
# 声明字符串
str_ = '少小离家老大回'
print(str_.startswith('少小'))
print(str_.startswith('少大'))


# endswith
# 作用：判断字符串是否以xxx结尾
# 语法：字符串.endswith（目标内容，开始位置，结束位置）
# 需求
# 声明字符串
print(str_.endswith('大回'))
print(str_.endswith('小回'))
# 注意：在Python中，起到判断作用的方法，方法调用后的返回值往往是布尔类型数据（True，False）


