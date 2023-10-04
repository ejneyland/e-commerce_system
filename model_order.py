import random
import datetime

class Order:
    
    existing_ids = set()

    @classmethod
    def generate_order_id(cls):
        while True:
            order_id = 'o_' + ''.join(str(random.randint(0, 9)) for _ in range(5))
            # checks that the generated id is not already in the existing_ids
            # if prod_id already exists >> loop restarts >> new prod_id generated and checked
            if order_id not in cls.existing_ids:
                # adds the uniquely generated id to the list of existing_ids
                cls.existing_ids.add(order_id)
                # if id is unique >> id is returned
                return order_id
        pass

    def __init__(self, user_id, prod_id):
        self.order_id = self.generate_order_id()
        self.user_id = user_id
        self.prod_id = prod_id
        self.order_time = self.retrieve_time_of_order() or "00-00-0000_00:00:00"

    def __str__(self):
        pass

    def save_to_file(self):
        pass

    @staticmethod
    def retrieve_time_of_order():
        # returns the current time in format 'DD-MM-YYYY_HH:MM:SS'
        order_time = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        return order_time