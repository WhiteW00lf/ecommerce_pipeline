from datetime import date
import pandas as pd
import random
import faker



def generate_products():
    product_dict = {
        "product_id": [],
        "product_name": [],
        "price": [],
        "stock": [],
        "category": []
    }
    products = ["Television", "Laptop", "Smartphone", "Headphones", "Camera", "Smartwatch", "Tablet", "Printer", "Monitor", "Speaker"]
    for product in range(1,2001):
        product_dict["product_id"].append(product)
        product_dict["product_name"].append(random.choice(products))
        product_dict["price"].append(round(random.uniform(500, 2000), 2))
        product_dict["stock"].append(random.randint(0, 100))
        product_dict["category"].append(random.choice(products))

    df = pd.DataFrame(product_dict)
    df.to_csv(f"data/raw/{date.today()}_products.csv", mode="a", index=False)
    print("Product data generated successfully.")


def generate_customers():
    customer_dict = {
        "customer_id": [],
        "first_name": [],
        "last_name": [],
        "address": [],
        "loyalty_tier": [],
        "last_updated": []

    }

    for customer in range(1, 2001):
        customer_dict["customer_id"].append(customer)
        customer_dict["first_name"].append(faker.Faker().first_name())
        customer_dict["last_name"].append(faker.Faker().last_name())
        customer_dict["address"].append(faker.Faker().address())
        customer_dict["loyalty_tier"].append(random.choice(["Bronze", "Silver", "Gold"]))
        customer_dict["last_updated"].append(faker.Faker().date_time_this_year())

    df = pd.DataFrame(customer_dict)
    df.to_csv(f"data/raw/{date.today()}_customers.csv", mode="a", index=False)
    print("Customer data generated successfully.")



def generate_orders():
    order_dict = {
        "order_id": [],
        "customer_id": [],
        "product_id": [],
        "quantity": [],
        "price": [],
        "order_date": [],
        "delivery_date": [],
        "status": []
    }

    for order in range(1, 2001):
        order_dict["order_id"].append(order)
        order_dict["customer_id"].append(random.randint(1, 2000))
        order_dict["product_id"].append(random.randint(1, 2000))
        order_dict["quantity"].append(random.randint(1, 5))
        order_dict["price"].append(round(random.uniform(500, 2000), 2))
        order_dict["order_date"].append(faker.Faker().date_time_this_year())
        order_dict["delivery_date"].append(faker.Faker().date_time_this_year())
        order_dict["status"].append(random.choice(["Pending", "Shipped", "Delivered", "Cancelled"]))

    df = pd.DataFrame(order_dict)
    df.to_csv(f"data/raw/{date.today()}_orders.csv", mode="a", index=False)
    print("Order data generated successfully.")




if __name__ == "__main__":
    generate_products()
    generate_customers()
    generate_orders()


