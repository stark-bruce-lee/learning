import random
num = random.randint(1, 100)
s = 1
guess_num = int(input("请输入一个数字："))
while guess_num != num:
    if guess_num > num:
        print("猜的数字大了")
    else:
        print("猜的数字小了。")
    s += 1
    guess_num = int(input("请再次输入一个数字："))
print("恭喜你猜对了，猜了%d次" % s)

