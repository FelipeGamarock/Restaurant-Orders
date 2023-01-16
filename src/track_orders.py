class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        orders = []
        for order in self.orders:
            if customer in order:
                orders.append(order[1])
        return max(set(orders), key=orders.count)

    def get_never_ordered_per_customer(self, customer):
        orders = []
        orders_options = {'hamburguer', 'pizza', 'misto-quente', 'coxinha'}
        for order in self.orders:
            if customer in order:
                orders.append(order[1])
        never_ordered = orders_options.difference(orders)
        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        days = []
        week_days = {'segunda-feira', 'terça-feira', 'sabado'}
        for order in self.orders:
            if customer in order:
                days.append(order[2])
        never_ordered = week_days.difference(days)
        return never_ordered

    def get_busiest_day(self):
        days = []
        for order in self.orders:
            days.append(order[2])
        return max(set(days), key=days.count)

    def get_least_busy_day(self):
        days = []
        for order in self.orders:
            days.append(order[2])
        return min(set(days), key=days.count)
