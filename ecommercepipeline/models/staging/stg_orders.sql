SELECT 
    order_id,
    customer_id,
    product_id,
    quantity,
    price,
    order_date::date AS order_date,
    delivery_date::date AS delivery_date,
    lower(status::text) AS status

FROM {{ source('raw', 'orders') }}

WHERE order_id IS NOT NULL