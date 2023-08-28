# 打开文件
f = open("D:/bill.txt", "r", encoding="UTF-8")
# 读取文件 - read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"读取所有文本的结果：{f.read()}")

# 读取文件-readlines()
# lines = f.readlines()  # 读取文件的全部行，封装到列表中
# print(f"lines对象的类型是：{type(lines)}")
# print(f"lines对象的结果是:{lines}")


# 读取文件-readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()
# print(f"第一行数据是:{line1}")
# print(f"第二行数据是:{line2}")
# print(f"第三行数据是:{line3}")
# print(f"第四行数据是:{line4}")

# for循环读取行
# for line in f:
#     print(line)

# 文件的关闭
# f.close()

# with open 语法操作文件 执行完自动关闭文件
with open("D:/bill.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(line)
