import random
num = random.randint(1, 10)
guess_num = int(input("请输入你猜的数字"))
if guess_num == num:
    print("恭喜你猜对了")
else:
    if guess_num < num:
        print("猜小了")
    else:
        print("猜大了")
    guess_num = int(input("请再次输入你猜的数字"))
    if guess_num == num:
        print("恭喜你猜对了")
    else:
        if guess_num < num:
            print("猜小了")
        else:
            print("猜大了")
        guess_num = int(input("请再次输入你猜的数字"))
        if guess_num == num:
            print("恭喜你猜对了")
        else:
            print("次数用完了")



# if guess_num == num:
#     print("恭喜你猜对了。")
# else:
#     if guess_num > num:
#         print("你猜的数字大了。")
#     else:
#         print("你猜的数字小了。")
#     guess_num = int(input("请再次输入你猜的数字"))
#     if guess_num == num:
#         print("恭喜你猜对了。")
#     else:
#         if guess_num > num:
#             print("你猜的数字大了。")
#         else:
#             print("你猜的数字小了。")
#     guess_num = int(input("请再次输入你猜的数字"))
#     if guess_num == num:
#         print("恭喜你猜对了。")
#     else:
#         print("很抱歉，猜测次数已用完。")

# if guess_num == num:
#     print("恭喜你，第一次猜对了。")
# elif guess_num > num:
#     print("猜的数字大了。")
# elif guess_num < num:
#     print("猜的数字小了。")
# guess_num = int(input("请再次输入你猜的数字"))
# if guess_num == num:
#     print("恭喜你，第二次猜对了。")
# elif guess_num > num:
#     print("猜的数字大了。")
# elif guess_num < num:
#     print("猜的数字小了。")
# guess_num = int(input("请再次输入你猜的数字"))
# if guess_num == num:
#     print("恭喜你第三次猜对了。")
# else:
#     print("三次机会用完了。")





