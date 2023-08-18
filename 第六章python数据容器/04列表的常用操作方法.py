# 1.1 查找某元素在列表内的下标索引
my_list = ["itcast", "itheima", "python"]
index = my_list.index("itheima")
print(f"itheima在列表中的下标索引值是：{index}")
# 1.2 查找的内容不存在会报错

# 2.修改特定下标索引的值
my_list[0] = "教育"
print(f"列表被修改元素值后，结果是：{my_list}")

# 3.指定下标位置插入新元素
my_list.insert(1, "best")
print(f"新的列表元素是：{my_list}")

# 4.在列表尾部添加新元素
my_list.append("黑马程序员")
print(f"新的列表元素是：{my_list}")

# 5.追加一批元素
my_list2 = [1, 2, 3]
my_list.extend(my_list2)
print(f"新的列表元素是：{my_list}")

# 6.删除指定下标索引的元素
my_list = ["itcast", "itheima", "python"]
# 6.1 方式1：del 列表[下标]
del my_list[2]
print(f"新的列表元素是：{my_list}")
# 6.2 方式2：列表.pop(下标)
my_list = ["itcast", "itheima", "python"]
element = my_list.pop(2)
print(f"新的列表元素是：{my_list}")

print(f"通过pop返回元素{element}")

# 7删除某元素在列表中的第一个匹配项
my_list = ["itcast", "itheima", "itcast", "itheima", "python"]
my_list.remove("itheima")
print(f"通过remove方法移除元素后，列表的结果是：{my_list}")

# 8清空列表
my_list = ["itcast", "itheima", "python"]
my_list.clear()
print(f"通过clear方法清空列表{my_list}")

# 9.统计列表内某元素的数量和元素的数量
number = [1, 1, 1, 2, 3, 4]
count = number.count(1)
count1 = len(number)
print(f"列表中1的数量是{count}")
print(f"列表中元素的数量是{count1}")


t9 = (1, 2, ["itheima", "itcast"])
print(f"t9的内容是: {t9}")
t9[2][0] = "黑马程序员"
t9[2][1] = "传智教育"
print(f"t9的内容是: {t9}")
