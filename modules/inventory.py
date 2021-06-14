import csv

class Inventory:
    
    def __init__(self, id, title, rating, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.copies_available = copies_available

    def __str__(self):
        return f"""
        Id: {self.id}
        Title: {self.title}
        Rating: {self.rating}
        Available Copies: {self.copies_available}
        """
    
    @classmethod
    def get_current_video_inventories(cls):
         with open("data/inventory.csv", 'r') as inventory_file:
            inventory_data = csv.DictReader(inventory_file)
            inventories = []
            for line in inventory_data:
                inventories.append(Inventory(**line).__dict__)
        
            return inventories
    def rent_video(self, title):
        pass