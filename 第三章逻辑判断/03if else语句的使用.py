print("欢迎来到游乐场，儿童免费，成人收费")
age = input("请输入你的年龄：")
age = int(age)
if age >= 18:
    print("你已经成年，需要补票10元")
else:
    print("你未成年，可以免费游玩")
print("祝你游玩愉快")
