"""
需求：
    1、程序实现打印商品列表，用户可通过编号来进行选购商品，允许不断的买商品。
    2、陈程序启动时，先让用户输入预购金额，总购物的商品金额不得超过预购金额
    3、用户可随时退出程序，退出时，打印分别买了哪些商品，以及剩余余额
"""

shop_list = [
    [1, 'iphone', 6999, 999],
    [2, 'mac air', 9999, 999],
    [3, 'macbook', 19999, 999],
    [4, 'T恤', 80, 999],
    [5, '小米电脑', 10999, 100]
]
shop_numbers = []
shopping_cart = []
balance = 0.0   # 预存金额
consumption = 0.00
print("和黑姑娘开始逛商场".center(100, "="))
for i in shop_list: print(f'编号:{i[0]},商品名称:{i[1]},商品价格：{i[2]},库存为：{i[3]}')
for j in shop_list:
    shop_numbers.append(j[0])
while True:
    balance = input('请输入你的预购金额>>>：').strip()
    if balance.isdigit():
        balance = float(balance)
        consumption = balance
        while True:
            shop_number = input('请输入需要购买商品的编号(如果输入00表示退出)：').strip()
            if not shop_number.isdigit():
                print('商品的编号输入错误')
                continue
            shop_number = int(shop_number)
            if shop_number == 00:  # 当输入00时表示退出了
                for j in shopping_cart: print(f"购买的商品：{j[1]},数量为：{j[2]}")
                print(f'本次共消费{consumption-balance},剩余余额为：{balance} 元')
                print("与黑姑娘购物结束".center(100, "="))
                exit()
            else:
                # 判断输入的编号是否在范围内
                if shop_number in shop_numbers:
                    count = 1  # 默认只购买一件
                    for k in shop_list:
                        # 库存不能小于0 并且购买的金额不能大于预购金额
                        if k[0] == shop_number:
                            if (k[3] > 0) and ((k[2] * count) < balance):
                                # 将商品的编号和名称加入购物车
                                shopping_cart.append([k[0], k[1], count])
                                balance = balance - (k[3] * count)  # 余额
                                k[3] = k[3] - count  # 库存
                                print(f"购买的商品列表{shopping_cart},余额还剩{balance}")
                                continue
                            else:
                                print(f'商品的库存或者余额不足,{k[0]}号商品库存为：{k[3]},你的余额为{balance}')
                else:
                    print('请输入正确的商品编号')
                    continue
    else:
        print('预购金额输入错误')
        continue

