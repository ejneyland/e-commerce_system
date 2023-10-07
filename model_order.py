from operation_order import OrderOperation

class Order:

    def __init__(self, user_id, prod_id):
        self.order_id = OrderOperation.generate_order_id()
        self.user_id = user_id
        self.prod_id = prod_id
        self.order_time = OrderOperation.retrieve_time_of_order() or "00-00-0000_00:00:00"

    def __str__(self):
        order_data = {
            'order_id': {self.order_id},
            'user_id': {self.user_id},
            'prod_id': {self.prod_id},
            'order_time': {self.order_id}
        }
        return str(order_data)