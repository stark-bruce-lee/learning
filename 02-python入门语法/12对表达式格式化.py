"""
演示对表达式进行字符串格式化
"""
print("1*1的结果是：%d" % (1*1))
print(f"1*2的结果是：{1*2}")
print("字符串在python中的类型名是：%s" % type("字符串"))


name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司:{name},股票代码:{stock_code},当前股价：{stock_price}")
print("每日增长系数是：%f，经过7天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor,stock_price*stock_price_daily_growth_factor**7))


