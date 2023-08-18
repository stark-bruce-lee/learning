# 第二种字符串格式化的方式：f”{占位}“
name = "传智播客"
set_up_year = 2006
stock_price = 19.99
# f：format格式化
print(f"我是{name}，我成立于{set_up_year}年，我今天的股票是{stock_price}元")
# 特点：不理会类型，不做精度控制，适合对精度没有要求时使用

