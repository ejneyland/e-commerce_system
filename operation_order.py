import random
import datetime

class OrderOperation:
    
    existing_ids = set()

    @staticmethod
    def generate_order_id():
    # def generate_unique_order_id():
        while True:
            order_id = 'o_' + ''.join(str(random.randint(0, 9)) for _ in range(5))
            # checks that the generated id is not already in the existing_ids
            # if prod_id already exists >> loop restarts >> new prod_id generated and checked
            if order_id not in OrderOperation.existing_ids:
                # adds the uniquely generated id to the list of existing_ids
                OrderOperation.existing_ids.add(order_id)
                # if id is unique >> id is returned
                return order_id
            
    def save_to_file(self):
        pass

    @staticmethod
    def retrieve_time_of_order():
        # returns the current time in format 'DD-MM-YYYY_HH:MM:SS'
        order_time = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        return order_time
    
    def create_an_order(customer_id, product_id, create_time):
        pass # return True/False

    def delete_order(order_id):
        pass # return True/False
    
    def get_order_list(customer_id, page_number):
        pass # returns tuple
    # including a list of order objects and the total number of pages. 
    # e.g. ([Order(), Order(), Order()...], page_number, total_page)

    def generate_test_order_data():
        pass

    def generate_single_customer_consumption_figure(customer_id):
        pass

    def generate_all_customer_consumption_figure():
        pass

    def generate_all_top_10_best_sellers_figure():
        pass

    def delete_all_orders():
        pass