# 统计字符串的长度，且不使用内置函数len()
str1 = "itheima"
str2 = "itcast"
str3 = "python"
def my_len(data):
    count = 0
    for x in data:
        count += 1
    print(f"字符串{data}有{count}个字符")
my_len(str1)
my_len(str2)
my_len(str3)