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
    def __init__(self):
        self.logged = None
        self.logged_in = False
    def main_menu(self):
        return int(input("""
            1. View video inventory
            2. View customer's rented videos
            3. Rent video
            4. Return video
            5. Add new customer
            6. Exit
        """))
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