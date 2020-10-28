# 手工输入 5 个学生的名字，存储到列表中，然后打印所有学生名字
# 提示: 先声明空列表, 循环添加学生名字
import random

list1 = []
# 定义计数器
num = 0
while num < 5:
    list1.append(input('请输入学生姓名:'))
    num += 1
for i in list1:
    print(i)

print(list1[random.randrange(len(list1))])
print(random.randrange(len(list1)))


