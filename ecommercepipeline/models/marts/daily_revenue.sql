SELECT 
    order_date,
    SUM(total_order_value) AS daily_revenue,
    count(DISTINCT order_id) AS daily_orders,
    COUNT(DISTINCT customer_id) AS unique_customers

FROM {{ ref('fct_orders') }}
WHERE status != 'cancelled'
GROUP BY order_date 
ORDER BY order_date ASC