# 定义字典
my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是:{my_dict1}, 类型是:{type(my_dict1)}")
print(f"字典2的内容是:{my_dict2}, 类型是:{type(my_dict2)}")
print(f"字典3的内容是:{my_dict3}, 类型是:{type(my_dict3)}")

# 定义重复key的字典
# 字典key不能重复
# my_dict1 = {"王力宏": 99, "王力宏": 88, "周杰伦": 88, "林俊杰": 77}

# 基于key获取value
score = my_dict1["王力宏"]
print(f"王力宏的考试分数是:{score}")

# 定义嵌套的字典
stu_score_dict = {
    "王力宏": {"语文": 77, "数学": 66, "英语": 33},
    "周杰伦": {"语文": 88, "数学": 86, "英语": 55},
    "林俊杰": {"语文": 99, "数学": 96, "英语": 66}
}

# 嵌套字典中获取数据
print(stu_score_dict["王力宏"]["语文"])
