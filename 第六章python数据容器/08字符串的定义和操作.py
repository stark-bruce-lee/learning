my_str = "itheima and itcast"
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串my_str取下标为2的元素,值是: {value},取下标为-16的元素。值是: {value2}")
# index查找下标索引
value = my_str.index("and")
print(f"在字符串{my_str}中查找and，其起始下标是:{value}")

# 字符串的替换
# 语法: 字符串.replace(字符串1，字符串2)
# 功能:将字符串内的全部:字符串1,替换为字符串2
# 注意: 不是修改字符串本身，而是得到了一个新字符串哦
new_my_str = my_str.replace("it", "程序")
print(f"原字符串{my_str}替换后的新字符串是{new_my_str}")

# 字符串的分割
# 语法: 字符串.split(分隔符字符串)
# 功能: 按照指定的分隔符字符串，
# 将字符串划分为多个字符串，
# 并存人列表对象中
# 注意:字符串本身不变，而是得到了一个列表对象

my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split分割后得到：{my_str_list},类型是：{type(my_str_list)}")

# strip方法
# 字符串规整
my_str = "  itheima and itcast   "
new_my_str = my_str.strip()
# 不传入参数，默认去除首尾空格
print(f"字符串{my_str}被strip后，结果：{new_my_str}")

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip后，结果：{new_my_str}")

# 统计字符串中某元素出现的次数,count法
my_str = "itheima and itcast"
num = my_str.count("it")
print(num)

# 统计字符串的长度 len法
my_str = "itheima and itcast"
num = len(my_str)
print(num)