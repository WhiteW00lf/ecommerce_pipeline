CREATE SCHEMA "raw";
CREATE SCHEMA "staging";

CREATE SCHEMA "marts";

CREATE TYPE loyalty_tier_type AS ENUM ('Bronze', 'Silver', 'Gold');
CREATE TYPE product_category_type AS ENUM ('Television', 'Laptop', 'Smartphone', 'Headphones', 'Camera', 'Smartwatch', 'Tablet', 'Printer', 'Monitor', 'Speaker');

CREATE TYPE order_status_type AS ENUM ('Pending', 'Shipped', 'Delivered', 'Cancelled');
CREATE TABLE "raw".customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    address TEXT NOT NULL,
    loyalty_tier loyalty_tier_type 
);

CREATE TABLE "raw".products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    category product_category_type 
);


CREATE TABLE "raw".orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    order_date TIMESTAMP NOT NULL,
    delivery_date TIMESTAMP NOT NULL,
    status order_status_type, 
    FOREIGN KEY (customer_id) REFERENCES "raw".customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES "raw".products(product_id)


)