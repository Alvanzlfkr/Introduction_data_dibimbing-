from order import Order
from order_processor import OrderProcessor


pesanan1 = Order("001", "Budi", "2024-01-01", 100000)
pesanan2 = Order("002", "Isal", "2024-01-02", 200000)
pesanan3 = Order("003", "Arfi", "2024-01-03", 150000)

prosesor = OrderProcessor()

prosesor.add_order(pesanan1)
prosesor.add_order(pesanan2)
prosesor.add_order(pesanan3)
prosesor.display_order()

revenue = int(prosesor.calculate_total_revenue())
pajak = int(prosesor.calculate_total_tax(0.10))

print(f"Total Revenue: {revenue}")
print(f"Total pajak: {pajak}")