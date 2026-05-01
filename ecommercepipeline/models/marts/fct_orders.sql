SELECT 
    o.order_id,
    o.customer_id,
    c.first_name,
    c.last_name,
    o.product_id,
    p.product_name,
    o.quantity,
    o.price AS order_price,
    p.price AS product_price,
    o.order_date,
    o.delivery_date,
    o.status,
    o.quantity * o.price AS total_order_value

FROM {{ ref('stg_orders') }} AS o
JOIN {{ ref('stg_customers') }} AS c ON o.customer_id = c.customer_id
JOIN {{ ref('stg_products') }} AS p ON o.product_id = p.product_id
