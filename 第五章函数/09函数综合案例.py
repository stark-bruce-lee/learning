# 定义全局变量 money name
money = 5000000
name = input("请输入你的名字：")
# 定义查询函数
def query():
    print("----------查询余额----------")
    print(f"{name}你好，你的余额剩余{money}元")
# 定义存款函数
def saving(num):
    print("----------存款----------")
    global money
    money += num
    print(f"{name}你好，你存款{num}元成功")
    print(f"{name}你好，你的余额剩余：{money}元")
def get_money(num):
    print("----------取款----------")
    global money
    money -= num
    print(f"{name}你好，你取款{num}元成功")
    print(f"{name}你好，你的余额剩余：{money}元")
def main():
    print(f"{name}你好，欢迎来到ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    key = input("请输入你的选择：")
    return key
while True:
    key = main()
    if key == "1":
        query()
        continue
    elif key == "2":
        num = int(input("请输入你要存入的金额"))
        saving(num)
        continue
    elif key == "3":
        num = int(input("请输入你要取走的金额"))
        get_money(num)
        continue
    else:
        break



