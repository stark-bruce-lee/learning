# if int(input("你的身高是多少：")) > 120:
#     print("身高超出限制，不可以免费。")
#
#     if int(input("你的vip级别是多少：")) > 3:
#         print("恭喜你，vip级别达标，可以免费")
#     else:
#         print("你需要买票10元")
# else:
#     print("欢迎小朋友，免费游玩")

age = 28
year = 2
level = 4
if age > 18:
    print("你是成年人了。")
    if age < 30:
        print("年龄达标了")
        if year > 2:
            print("入职时间和年龄均达标了，可以领取")
        elif level > 3:
            print("级别和年龄均达标了，可以领取")
        else:
            print("入职时间或者级别不够，无法领取")
    else:
        print("年龄太大了，无法领取")
else:
    print("小朋友无法领取")
