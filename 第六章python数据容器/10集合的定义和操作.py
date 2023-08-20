# 定义集合
my_set = {"传智教育", "黑马程序员", "ithrima"}
my_set_empty = set()
print(f"my_set的内容是：{my_set},类型是{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty},类型是{type(my_set_empty)}")

# 添加新元素
my_set = {"传智教育", "黑马程序员", "ithrima"}
my_set.add("Python")
print(f"my_set添加元素后结果是：{my_set}")

# 移除元素
# print(f"my_set添加元素后结果是：{my_set}")
my_set.remove("传智教育")
print(f"my_set移除元素后结果是：{my_set}")

# 随机取出一个元素
# pop

# 清空集合，clear

# 取两个集合的差集
# 取出2个集合的差集
# 语法:集合1.difference(集合2)，
# 功能:取出集合1和集合2的差集（集合1有而集合2没有的）
# 结果:得到一个新集合，集合1和集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(set3)
print(set1)
print(set2)

# 消除2个集合的差集
# 语法:集合1.difference update(集合2)
# 功能:对比集合1和集合2，在集合1内，删除和集合2相同的元素
# 结果:集合1被修改，集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(set1)
print(set2)

# 2个集合合并
# 语法:集合1.unior(集合2)
# 功能:将集合1和集合2组合成新集合
# 结果: 得到新集合，集合1和集合2不变
setl = {1, 2, 3}
set2 = {1, 5, 6}
set3 = setl.union(set2)
print(set3)
print(set1)
print(set2)
# 结果: {1，2，3，5，6]，新集合
# 结果:{1，2，3}，set1不变
# 结果:{1，5，6]，set2不变

# 统计集合元素数量len()

# 遍历用for循环进行
