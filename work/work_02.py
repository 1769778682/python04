# 1. 现有字符串信息如下: 少小离家老大回,乡音无改鬓毛衰,儿童相见不相识,笑问客从何处来
# 2. 将该字符串处理后, 按照如下格式输出到控制台:
# 少小离家老大回
# 乡音无改鬓毛衰
# 儿童相见不相识
# 笑问客从何处来

# 提示: 可以考虑 split() 方法和循环遍历
str1 = '少小离家老大回,乡音无改鬓毛衰,儿童相见不相识,笑问客从何处来'
list1 = str1.split(',')
print(list1)
for i in list1:
    print(i)