import csv

class Customer:
    
    def __init__(self,id,first_name,last_name,current_video_rentals):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.rented_videos = current_video_rentals


    def __str__(self):
        return f"""
        Id: {self.id}
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Rented Videos: {self.rented_videos}
        """
        
    @classmethod
    def get_all_customers(cls):
         with open("data/customers.csv", 'r') as customer_file:
            customer_data = csv.DictReader(customer_file)
            customers = []
            for line in customer_data:
                customers.append(Customer(**line).__dict__)
        
            return customers