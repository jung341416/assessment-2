from modules.customer import Customer
from modules.inventory import Inventory
import csv



class Store:
    
    
    def __init__(self):
        self.customers = Customer.get_all_customers()
        self.inventories = Inventory.get_all_inventories()
    
    
    def view_inventories(self):
        for inventory in self.inventories:
            print(f"ID: {inventory.id}, TITLE: {inventory.title}, RATING: {inventory.rating}, AVAILABLE COPIES: {inventory.copies_available}.")
    
    
    def view_current_customer_video(self, customer_id):
        target_customer = []
        with open('data/customers.csv', 'r') as csv_file:
            data = csv.DictReader(csv_file)
            for row in data:
                customer = Customer(**dict(row))
                if customer.id == customer_id:
                    target_customer.append(customer)
            for customer in target_customer:
                if customer.current_video_rentals == "":
                    print(f"{customer.first_name} {customer.last_name}'s didn't rent any videos")
                else:
                    print(f"{customer.first_name} {customer.last_name}'s current rental lists: {customer.current_video_rentals}")
    
    
    
    def add_new_customer(self, customer_data):
        new_customer = Customer(**customer_data)
        for customer in self.customers:
            if new_customer.id == customer.id:
                print("ID's already taken!")
                return
        print('new customer created!')
        self.customers.append(new_customer)
        self.save_change_customer_data()
    
    
    def rent_video_to_customer(self, input_id, title):
        for inventory in self.inventories:
            if inventory.title == title and int(inventory.copies_available) >0:
                inventory.copies_available = int(inventory.copies_available) - 1
            elif inventory.title == title and int(inventory.copies_available) == 0:
                print(f'{title} is not in stock!')
                return
        self.save_change_inventory_data()
        for customer in self.customers:
            video_counts = len(customer.current_video_rentals.split('/'))
            if customer.id == input_id and customer.current_video_rentals == "":
                customer.current_video_rentals += title
            elif customer.id == input_id and video_counts < 3:
                customer.current_video_rentals += f"/{title}"
            elif customer.id == input_id and video_counts >= 3:
                print('customer can only have 3 maximum videos!')
        self.save_change_customer_data()
        
  
    
    
    def return_video_to_store(self, input_id, title):
        for customer in self.customers:
            video_counts = len(customer.current_video_rentals.split('/'))
            video_lists = customer.current_video_rentals.split('/')
            if customer.id == input_id and customer.current_video_rentals == "":
                print(f"{customer.first_name} didn't rent {title}")
                return
            elif customer.id == input_id and video_counts == 1:
                new_title = customer.current_video_rentals.replace(title, "")
                customer.current_video_rentals = new_title
            elif customer.id ==input_id and video_lists[0] == title and video_counts > 1:
                new_title =customer.current_video_rentals.replace(f"{title}/", "")
                customer.current_video_rentals = new_title
            elif customer.id == input_id and video_counts > 1:
                new_title = customer.current_video_rentals.replace(f"/{title}", "")
                customer.current_video_rentals = new_title
        self.save_change_customer_data()
        for inventory in self.inventories:
            if inventory.title == title:
                inventory.copies_available = int(inventory.copies_available) + 1
                print(f"{title} is returned!")
        print(f"{title} is not in stock!")
        self.save_change_inventory_data()
    
    
    
    def save_change_customer_data(self):
        with open('data/customers.csv', 'w') as csv_file:
            fields = ['id','first_name','last_name','current_video_rentals']
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(fields)
            for customer in self.customers:
                csvwriter.writerow([customer.id, customer.first_name, customer.last_name, customer.current_video_rentals])        
    
    
    
    def save_change_inventory_data(self):
        with open('data/inventory.csv', 'w') as csv_file:
            fields = ['id','title','rating','copies_available']
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(fields)
            for inventory in self.inventories:
                csvwriter.writerow([inventory.id, inventory.title, inventory.rating, inventory.copies_available])