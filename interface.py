from modules.store import Store

my_store = Store()

while True:
    user_input = input(f"""Welcome to Code Platoon Video!
    1. View video inventory
    2. View customer's rented videos
    3. Rent video
    4. Return video
    5. Add new customer
    6. Exit
    """)
    if user_input == '1':
        my_store.view_inventories()
    elif user_input == '2':
        customer_id = input('Enter Customer ID: ')
        my_store.view_current_customer_video(customer_id)
    elif user_input == '3':
        customer_id = input('Enter Customer ID: ')
        inventory_title = input('Enter Video Title for Rent: ')
        my_store.rent_video_to_customer(customer_id, inventory_title)
    elif user_input == '4':
        customer_id = input('Enter Customer ID: ')
        inventory_title = input('Enter Video Title to Return: ')
        my_store.return_video_to_store(customer_id, inventory_title)
    elif user_input == '5':
        customer_data = {}
        customer_data['id'] = input('Enter Customer ID: ')
        customer_data['first_name'] = input('Enter Customer First Name: ')
        customer_data['last_name'] = input('Enter Customer Last Name: ')
        customer_data['current_video_rentals'] = ""
        my_store.add_new_customer(customer_data)
    elif user_input == '6':
        break    

