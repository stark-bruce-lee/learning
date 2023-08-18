t1 = ("周杰伦", 11, ["football", "music"])
index = t1.index(11)
print(f"年龄所在的下标位置是{index}")
name = t1[0]
print(f"学生的姓名是{name}")
del t1[2][0]
print(f"删掉学生爱好中的football后，新的元组是{t1}")
# 增加爱好：coding到爱好list内

