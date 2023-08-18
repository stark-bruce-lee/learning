# range语法1
# for x in range(10):
#     print(x)
# range语法2
# for x in range(5,10):
#     print(x)
# range语法3
# for x in range(5, 10, 2):
#     print(x)
s = 0
for x in range(1, 101):
    if x % 2 == 0:
        s += 1
print(s)