class IOInterface:
    def get_user_input(prompt, num_of_args):
        user_input = input(prompt).split()
        return user_input + [''] * (num_of_args - len(user_input))

    def main_menu():
        print("""
e-commerce information system
------------------------
1. Login
2. Register
3. Quit
------------------------
        """, end=' ')

    def admin_menu():
        print("""
------------------------
1. Show Products
2. Add Customers
3. Show Customers
4. Show Orders
5. Generate Test Data
6. Generate all statistical figures
7. Delete All Data
8. Logout
------------------------
        """, end=' ')

    def customer_menu():
        print("""
------------------------
1. Show Profile
2. Update Profile
3. Show Products
4. Show Order History
5. Generate all consumption figures
6. Logout
------------------------
        """, end=' ')

    def show_list(user_role, list_type, object_list):
        pass
        # object lists: Customer, Product, Order
        # user_role = "customer"
            # only product lists and personal orders list displayed
        # user_role = "admin"
            # all lists can be displayed

    def print_error_message(error_source, error_message):
        print(f"Error in {error_source}: {error_message}")

    def print_message(message):
        print(message)

    def print_object(target_object):
        print(str(target_object))