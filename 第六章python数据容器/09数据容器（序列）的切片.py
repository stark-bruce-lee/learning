# 语法: 序列[起始下标:结束下标:步长]
# 表示从序列中，从指定位置开始，依次取出元素，到指定位置结束，得到一个新序列:
# 起始下标表示从何处开始，可以留空，留空视作从头开始
# 结束下标(不含)表示何处结束，可以留空，留空视作截取到结尾步长表示，依次取元素的间隔
# 步长1表示，一个个取元素
# 步长2表示，每次跳过1个元素取
# 步长N表示，每次跳过N-1个元素取
# 步长为负数表示，反向取(注意，起始下标和结束下标也要反向标记)


# 对list进行切片，从1开始，4结束，步长为1
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4]
print(f"结果1：{result1}")

# 对tuple进行切片，从头开始，到最后结束，步长为1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]
print(f"结果2：{result2}")

# 对str进行切片，从头开始，到最后结束，步长为2
my_str = "01234567"
result3 = my_str[::2]
print(f"结果3：{result3}")

# 对str进行切片，从头开始，到最后结束，步长为-1
my_str = "01234567"
result4 = my_str[::-1]
print(f"结果4：{result4}")

# 对list进行切片，从3开始，1结束，步长为-1
my_list = [0, 1, 2, 3, 4, 5, 6]
result5 = my_list[3:1:-1]
print(f"结果5：{result5}")

# 对tuple进行切片，从头开始，到最后结束，步长为-2
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result6 = my_tuple[::-2]
print(f"结果6：{result6}")