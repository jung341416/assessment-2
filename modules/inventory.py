import csv
class Inventory:
    
    def __init__(self, id, title, rating, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.copies_available = copies_available
    def __str__(self):
        return f"""
            ID: {self.id}
            TITLE: {self.title}
            RATING: {self.rating}
            AVAILABLE_COPIES: {self.copies_available}
            """
    @classmethod
    def get_all_inventories(cls):
        inventories = []
        with open('data/inventory.csv', 'r') as csv_file:
            inventory_data = csv.DictReader(csv_file)
            for line in inventory_data:
                inventories.append(Inventory(**dict(line)))
        return inventories