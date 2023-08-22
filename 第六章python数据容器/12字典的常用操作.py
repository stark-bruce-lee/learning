# 新增更新元素
my_dict1 = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
my_dict1["张信哲"] = 66
my_dict1["周杰伦"] = 33
print(f"字典经过新增和更新元素后,结果：{my_dict1}")

# 删除元素
score = my_dict1.pop("周杰伦")
print(f"周杰伦的成绩为:{score},因作弊被删除后的字典为:{my_dict1}")

# 清空元素
my_dict1 = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
my_dict1.clear()
print(my_dict1)

# 获取全部的key
my_dict1 = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
keys = my_dict1.keys()
print(keys)

# 遍历字典
for key in keys:
    print(f"字典的key是:{key}")
    print(f"字典的value是:{my_dict1[key]}")


for key in my_dict1:
    print(f"2字典的key是:{key}")
    print(f"2字典的value是:{my_dict1[key]}")

# 统计字典的元素数量 len()





