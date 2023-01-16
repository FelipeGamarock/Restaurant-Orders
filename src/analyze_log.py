import csv


def analyze_log(path_to_file):
    if '.csv' not in path_to_file:
        raise FileNotFoundError(f'Extensão inválida. {path_to_file}')
    try:
        with open(path_to_file) as file:
            info = list(csv.reader(file))
            orders_by_maria = get_orders_food(info, 'maria')
            maria_most_ordered = get_most_ordered(orders_by_maria)
            orders_by_arnaldo = get_orders(info, 'arnaldo')
            arnaldo_burgues = food_counter(orders_by_arnaldo, 'hamburguer')
            orders_by_joao = get_orders(info, 'joao')
            food_not_order_joao = get_not_ordered_food(orders_by_joao, 'joao')
            days_not_order_joao = get_not_ordered_days(orders_by_joao, 'joao')
        with open('data/mkt_campaign.txt', "w") as final_file:
            final_file.write(
                f"{maria_most_ordered}\n"
                f"{arnaldo_burgues}\n"
                f"{food_not_order_joao}\n"
                f"{days_not_order_joao}\n"
            )

    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo inexistente. {path_to_file}')


def get_orders_food(info, name):
    orders_food = list()
    for order in info:
        if order[0] == name:
            orders_food.append(order[1])
    return orders_food


def get_orders(info, name):
    orders_by_name = list()
    for order in info:
        if order[0] == name:
            orders_by_name.append(order)
    return orders_by_name


def get_most_ordered(data):
    maria_most_ordered = max(set(data), key=data.count)
    return maria_most_ordered


def food_counter(info, food):
    aperrences = 0
    for order in info:
        if order[1] == food:
            aperrences += 1
    return aperrences


def get_not_ordered_days(orders, name):
    joao_visited_days = []
    week_days = {'segunda-feira', 'terça-feira', 'sabado'}
    for order in orders:
        if name in order:
            joao_visited_days.append(order[2])
    joao_never_visited = week_days.difference(joao_visited_days)
    return joao_never_visited


def get_not_ordered_food(orders, name):
    joao_orders = []
    orders_options = {'hamburguer', 'pizza', 'misto-quente', 'coxinha'}
    for order in orders:
        if name in order:
            joao_orders.append(order[1])
    joao_never_ordered = orders_options.difference(joao_orders)
    return joao_never_ordered
