# Write your solution here!

from modules.inventory import Inventory
from modules.customer import Customer
from interface import Interface

a = Customer(122,'Juing', 'Park', 'lionKing')
b = Inventory(1,'Guardians of the Galaxy','PG-13',5)
print(b.get_all_inventories())
print(a.get_all_customers())
# print(a.customer_current_rented_video('2'))
