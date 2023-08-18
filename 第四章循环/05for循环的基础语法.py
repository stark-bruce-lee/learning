# name = "李泽昊"
# for x in name:
#     print(x)
# 将name的内容挨个取出赋予x临时变量
count = 0
name = "itheima is a brand of itcast"
for x in name:
    if x == "a":
        count += 1
print(f"{name}中含有：{count}个字母a")


