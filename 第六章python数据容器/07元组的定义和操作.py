# 定义元组
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是:{type(t1)},内容是:{t1}")
print(f"t2的类型是:{type(t2)},内容是:{t2}")
print(f"t3的类型是:{type(t3)},内容是:{t3}")
# 定义单个元素的元组
t4 = ("Hello", )
print(f"t4的类型是:{type(t4)},内容是:{t4}")
# 元组的嵌套定义
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是:{type(t5)},内容是:{t5}")
# 下标索引取出元素
num = t5[1][2]
print(f"从t5中取出的元素是{num}")

# 元组的操作:index查找方法
t6 = ("传智教育", "黑马程序员", "Python")
index = t6.index("黑马程序员")
print(f"在元组t6中查找黑马程序员，的下标是: {index}")

# 元组的操作:count统计方法
t7 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "Python")
num = t7.count("黑马程序员")
print(f"在元组t7中统计黑马程序员的数量有: {num}个")

# len函数统计元组中元素的数量
t8 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "Python")
num = len(t8)
print(f"t8元组中元素的数量是{num}个")
