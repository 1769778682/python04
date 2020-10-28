str_data = 'abcdefgh'
# 获取cde
print(str_data[2:5:1])  # 切片结束索引对应的值不在范围内
print(str_data[2:5])  # 默认步长就是1，一般情况下可以省略
print(str_data[:5])  # 如果不给结束索引，默认从0开始
print(str_data[2:])  # 如果不给结束索引，则默认到结尾（-1）
print(str_data[:])  # 如果同时不给开始和结束索引，默认所有内容
print(str_data[::2])  # 步长：间隔数量（前面的两个冒号不可省略）
print(str_data[:-1])  # 代表倒数的第一个数据
print(str_data[::-1])  # 倒序输出字符串（特殊，记住即可）


