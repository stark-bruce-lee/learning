number = [21, 25, 21, 23, 22, 20]
number.append(31)
print(number)

number = [21, 25, 21, 23, 22, 20]
number1 = [29, 33, 30]
number.extend(number1)
print(number)

number = [21, 25, 21, 23, 22, 20]
number2 = number.pop(0)
# number3 = number.pop(5)
print(number2)
# print(number3)
#
number = [21, 25, 21, 23, 22, 20]
index = number.index(21)
print(index)