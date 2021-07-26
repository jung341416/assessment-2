import csv

class Customer:
    def __init__(self,id,first_name,last_name,current_video_rentals):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals
    def __str__(self):
        return f"""
            ID: {self.id}
            FIRST_NAME: {self.first_name}
            LAST_NAME: {self.last_name}
            VIDEO_RENTED: {self.current_video_rentals}
        """
        
    @classmethod
    def get_all_customers(cls):
         with open("data/customers.csv", 'r') as customer_file:
            customer_data = csv.DictReader(customer_file)
            customers = []
            for line in customer_data:
                customers.append(Customer(**dict(line)))
            return customers