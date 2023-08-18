money = 10000
for i in range(1, 21):
    import random
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}绩效{score}低于5，不发工资，下一位")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}，满足条件发放工资1000元，账户余额还有：{money}元")
    else:
        print("余额不足，不发了")
        break

