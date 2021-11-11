ings = ["x 25", "y 20", "z 1000"]
menu = ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"]
sell = ["BBBB 3", "TTT 2"]


def calculateNetIncome(ings, menu):
    ing_dic = {}
    for el in ings:
        tmp = el.split(' ')
        ing_dic[tmp[0]] = int(tmp[1])
    # print(ing_dic)
    menu_netincome = {}
    for el in menu:
        tmp = el.split(' ')
        ings_cost = 0
        name, ings, price = tmp[0], tmp[1], int(tmp[2])
        for ing in ings:
            ings_cost += ing_dic[ing]
        menu_netincome[name] = price-ings_cost

    return menu_netincome


def calculateProfit(menu_netincome, sell):
    total = 0
    for el in sell:
        tmp = el.split(' ')
        menu, amount = tmp[0], int(tmp[1])
        total += menu_netincome[menu]*amount
    print(total)
    return total


def solution(ings, menu, sell):
    menu_netincome = calculateNetIncome(ings, menu)
    return calculateProfit(menu_netincome, sell)


solution(ings, menu, sell)
