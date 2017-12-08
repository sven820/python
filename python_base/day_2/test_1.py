__author__ = "JJ.sven"

product_list = [
    ["iPhone", 5000],
    ["mac pro", 10000],
    ["Watch", 3200],
    ["Book", 288],
    ["bike", 2889],
]

money = 0
shop_list = []
exit_step = "q"

money = input("your all money:")
if money.isdigit():
    money = int(money)
else:
    money = 0
    print('输入金额不正确，程序退出')

if money > 0:
    while True:
        print('=======欣欣超市========================')
        for index, item in enumerate(product_list):
            print(index, item)

        index_buy = input("请输入商品编号购买：")
        if index_buy.isdigit():
            index_buy = int(index_buy)
            if index_buy >= len(product_list):
                print('编号输入不正确')
                continue;
            sel_shop = product_list[index_buy];
            item_money = sel_shop[1]
            item_name = sel_shop[0]
            if item_money < money:
                shop_list.append(sel_shop)
                money -= item_money
                print(item_name, "已加入购物车")
            else:
                print('钱不够，只剩：', money)

            step = input("请输入操作（q退出，否则继续）")
            if step == exit_step:
                print('您的余额为', money, ', 欢迎下次回顾，您的物品请拿好：')
                for index, item in enumerate(shop_list):
                    print(index, item)
                break;
        else:
            print("编号输入不正确")
            continue;
