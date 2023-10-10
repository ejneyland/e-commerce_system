class Order:

    # Order Costructor method
    def __init__(self, order_id, user_id, prod_id, order_time):
        self.order_id = order_id
        self.user_id = user_id
        self.prod_id = prod_id
        self.order_time = order_time or "00-00-0000_00:00:00"

    # Order Str Object method
    def __str__(self):
        # defines a dictionary of Order attributes, key-value pairs
        order_data = {
            'order_id': {self.order_id},
            'user_id': {self.user_id},
            'prod_id': {self.prod_id},
            'order_time': {self.order_id}
        }
        # returns a string representation of the Order instance/object
        return str(order_data)
    
# ------------------------------------------------------------