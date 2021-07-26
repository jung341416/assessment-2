import unittest
from modules.store import Store
from modules.customer import Customer
from modules.inventory import Inventory
class Store_Test_Suite(unittest.TestCase):
    def test_customer_list(self):
        customer_test = Customer.get_all_customers()
        store_test = Store().customers
        self.assertEqual(customer_test, store_test)



if __name__ == "__main__":
    unittest.main()