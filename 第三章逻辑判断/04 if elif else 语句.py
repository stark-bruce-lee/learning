
"""
print("欢迎来到动物园")
height = int(input("请输入你的身高(cm):"))
vip_level = int(input("请输入你的VIP等级(1~5):"))
if height < 120:
    print("你可以免费游玩。")
elif vip_level > 3:
    print("你的VIP级别大于3，可以免费游玩。")
else:
    print("不好意思，所有条件都不满足，需要购票10元。")
print("祝你游玩愉快。")
"""

if int(input("请输入你的身高(cm):")) < 120:
    print("身高小于120cm，可以免费。")
elif int(input("请输入你的VIP等级(1~5):")) > 3:
    print("vip等级大于3，可以免费。")
elif int(input("请告诉我今天记号：")) == 1:
    print("今天是1号免费日，可以免费。")
else:
    print("不好意思，条件都不满足，需要购票")

num = 5
if int(input("请输入一个数字：")) == num:
    print("恭喜你，猜对了。")
elif int(input("猜错了，在输入一个数字：")) == num:
    print("恭喜你，猜对了。")
elif int(input("最后一次机会，请输入一个数字：")) == num:
    print("恭喜你，猜对了。")
else:
    print("很遗憾，你猜错了。")
