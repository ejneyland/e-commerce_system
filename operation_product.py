import random

class ProductOperation:
    
    existing_ids = set()

    @staticmethod
    def generate_prod_id():
        # starts with 'p_' followed by 5 digits
        # e.g. 'p_01234'
        while True:
            prod_id = 'p_' + ''.join(str(random.randint(0, 9)) for _ in range(5))
            # checks that the generated id is not already in the existing_ids
            # if prod_id already exists >> loop restarts >> new prod_id generated and checked
            if prod_id not in ProductOperation.existing_ids:
                # adds the uniquely generated id to the list of existing_ids
                ProductOperation.existing_ids.add(prod_id)
                # if id is unique >> id is returned
                return prod_id

    @staticmethod
    def extract_products_from_files():
        with open("data/products.txt", "a") as file:
            for category in ["accessories", "bags", "beauty", "house", "jewelry", "kids", "men", "shoes", "women"]:
                with open(f"data/product/{category}.csv", "r") as csv_file:
                    for line in csv_file:
                        prod_data = line.strip().split(',')

                        prod_id = prod_data[-2]
                        prod_model = prod_data[-1]
                        prod_category = prod_data[0]
                        prod_name = prod_data[2]
                        prod_current_price = prod_data[3]
                        prod_raw_price = prod_data[4]
                        prod_discount = prod_data[6]
                        prod_likes_count = prod_data[7]

                        prod_data = f"{prod_id},{prod_model},{prod_category},{prod_name},{prod_current_price},{prod_raw_price},{prod_discount},{prod_likes_count}"
                        file.write(prod_data + '\n')

    @staticmethod
    def show_category_products(selection):

        with open("data/products.txt", "r") as file:
            products = [line.strip().split(',') for line in file]
    
        if selection == '1': # show accessories
            category = "accessories"
        elif selection == '2': # show bags
            category = "bags"
        elif selection == '3': # show beauty
            category = "beauty"
        elif selection == '4': # show house
            category = "house"
        elif selection == '5': # show jewelry
            category = "jewelry"
        elif selection == '6': # show kids
            category = "kids"
        elif selection == '7': # show men
            category = "men"
        elif selection == '8': # show shoes
            category = "shoes"
        elif selection == '9': # show women
            category = "women"
        else:
            "Inalid selection"

        category_products = [product for product in products if product[2] == category]

        if category_products:
            print(f"Products in the {category} category:")
            for product in category_products:
                print(f"ID: {product[0]}, Name: {product[3]}, Current Price: {product[4]}, Discount: {product[6]}")
        else:
            print(f"No products found in the {category} category.")
        

    @staticmethod
    def get_product_list(page_number):
        # retrieves one page of products from textfile, max. 10 items per page
        # return tuple
        # including a list of products objects and the total number of pages. 
        # e.g. ([Product1,Product2,Product3,...Product10],p age_number, total_page)
        with open("data/products.txt", "r") as file:
            products = [line.strip().split(',') for line in file]
            start_index = (page_number - 1) * 10
            end_index = min(page_number * 10, len(products))
            return products[start_index:end_index], page_number, len(products) // 10 + 1

    @staticmethod
    def delete_product(prod_id):
        deletion_successful = False
        with open("data/products.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                if line.strip().split(',')[0] == prod_id:
                    lines.remove(line)
                    deletion_successful = True

        with open("data/products.txt", "w") as file:
            file.writelines(lines)
        
        return deletion_successful
    
    @staticmethod
    def get_product_by_id(prod_id):
        with open("data/products.txt", "r") as file:
            for line in file:
                prod_data = line.strip().split(',')
                if prod_data[0] == prod_id:
                    return prod_data
            return None
    
    @staticmethod
    def delete_all_products():
        with open("data/products.txt", "w") as file:
            file.write("")

    # ---------------

    def generate_category_figure():
        pass
    # generates a bar chart showing the total numberof products for each category in a descending order
    # saving to data/figure folder

    def generate_discount_figure():
        pass
    # generates a pie chart that shows the proportion of products that have a discount value less than 30, between 30 and 60 inclusive, and greater than 60
    # saving to data/figure folder

    def generate_likes_count_figure():
        pass
    # generates a chart displaying the sum of products likes_count for each category in ascending order
    # saving to data/figure folder

    def generate_discount_likes_count_figure():
        pass
    # generates a scatter chart showing the relationship between likes_count and discount for all products
    # saving to data/figure folder

