def user_info(name, age, gender):
    print(f"姓名是:{name},年龄是:{age}, 性别是:{gender}")
# 位置参数——默认使用形式
user_info("小明", 20, "男")

# 关键字参数
user_info(name="小娜", age=19, gender="女")
user_info(age=10, gender="女", name="娜娜")


# 缺省参数
def user_info(name, age, gender="男"):
    print(f"姓名是:{name},年龄是:{age}, 性别是:{gender}")
user_info("小明", 20)
user_info(name="小娜", age=19, gender="女")


# 不定长——位置不定长 *号
# 不定长定义的形式参数会作为元组存在，接受不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)},内容是:{args}")
user_info(1, 2, 3, 'hello')

# 不定长——关键字不定长，**号
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)},内容是:{kwargs}")
user_info(name="娜娜", age=19, gender="女孩")