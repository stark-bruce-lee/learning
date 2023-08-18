# 使用print直接输出数据类型
print(type("C语言是最好的语言"))
print(type(666))
print(type(13.14))
# 使用变量存储type()语句的结果
string_type = type("C语言最好")
int_type = type(666)
float_type = type(13.14)
print(string_type)
print(int_type)
print(float_type)
# 使用type()语句，查看变量中存储的数据类型
name = "最厉害"
type(name)