# path = "C:\Users\sandysong\Desktop\就业班\新建文本文档 (2).txt"
# Windows系统下的文件路径信息中包含的'\'是转义字符
# 如果不处理，读取文件时可能会报错

# 方法一：使用转义字符：还原\本身的含义  # 重点
path = "C:\\Users\\sandysong\\Desktop\\就业班\\新建文本文档 (2).txt"
# 方法二：在路径字符串外侧添加"r",row  # 重点
path = r"C:\Users\sandysong\Desktop\就业班\新建文本文档 (2).txt"

str_data = 'I\'m lilei'
print(str_data)

