class OrderProcessor:
    def __init__(self):
        self.orders = []
    def add_order(self, order):
        self.orders.append(order)
    def calculate_total_revenue(self):
        total = 0
        for order in self.orders:
            total += order.total_amount
        return total
    def calculate_total_tax(self, tax_rate):
        total_tax = 0
        for order in self.orders:
            total_tax += order.calculate_tax(tax_rate)
        return total_tax
    def display_order(self):
        for order in self.orders:
            order.display_order()
            print()