# Welcome to Code Platoon Video!
# 1. View video inventory
# 2. View customer's rented videos
# 3. Rent video
# 4. Return video
# 5. Add new customer
# 6. Exit
import csv
from modules.customer import Customer
from modules.inventory import Inventory

class Interface:
    menu_options = [
        "1. View video inventory",
        "2. View customer's rented videos",
        "3. Rent video",
        "4. Return video",
        "5. Add new customer",
        "6. Exit"   
    ]
    def print_menu(self):
        print("Welcome to Code Platoon Video!:")
        for option in self.menu_options:
            print(option)
    def view_video_inventory(self):
        pass
    def view_customer_rented_videos(self):
        pass
    def rent_video(self):
        pass
    def return_video(self):
        pass
    def add_new_customer(self):
        pass